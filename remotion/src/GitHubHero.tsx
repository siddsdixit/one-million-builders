import React from "react";
import {
  AbsoluteFill,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";

const BG = "#fafafa";
const FG = "#0a0a0a";
const MUTED = "#6b6b6b";
const BORDER = "#e5e5e5";
const SURFACE = "#f0f0f0";
const FONT = "system-ui, -apple-system, BlinkMacSystemFont, sans-serif";

// ─── Act timing (780 frames = 26s @ 30fps) ───────────────────────────
const A1 = { s: 0,   e: 115  }; // Problem sentences
const A2 = { s: 120, e: 235  }; // AI Divide          (5f gap after A1)
const A3 = { s: 240, e: 400  }; // Blocks + quote     (5f gap after A2)
const A4 = { s: 405, e: 555  }; // One million [role] (5f gap after A3)
const A5 = { s: 560, e: 660  }; // 18-day journey     (5f gap after A4, 100f)
const A6 = { s: 672, e: 790  }; // Counter            (12f gap after A5, 118f)
const A7 = { s: 802, e: 910  }; // CTA + close        (12f gap after A6, 108f)

// ─── Helpers ──────────────────────────────────────────────────────────
function fi(frame: number, start: number, dur = 10) {
  return Math.max(0, Math.min(1, (frame - start) / Math.max(1, dur)));
}
function fo(frame: number, end: number, dur = 10) {
  return Math.max(0, Math.min(1, (end - frame) / Math.max(1, dur)));
}
function show(frame: number, s: number, e: number, i = 8, o = 8) {
  return Math.min(fi(frame, s, i), fo(frame, e, o));
}

// ─── Builder Blocks SVG logo ──────────────────────────────────────────
function BuilderBlocks({ size = 40, progress = 1 }: { size?: number; progress?: number }) {
  const sc = size / 32;
  const r = Math.max(1, 1.5 * sc);
  const blocks = [
    { x: 4,  y: 20, d: 0,    a: 1   },
    { x: 18, y: 20, d: 0.15, a: 1   },
    { x: 11, y: 10, d: 0.3,  a: 1   },
    { x: 11, y: 0,  d: 0.5,  a: 0.4 },
  ];
  return (
    <svg width={size} height={size} viewBox="0 0 32 32" fill="none">
      {blocks.map((b, i) => {
        const lp = Math.max(0, Math.min(1, (progress - b.d) / 0.3));
        return (
          <rect key={i} x={b.x} y={b.y} width={10} height={8} rx={r / sc}
            fill={FG} opacity={b.a * lp}
          />
        );
      })}
    </svg>
  );
}

function Logo({ size = 48, opacity = 1 }: { size?: number; opacity?: number }) {
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 14, opacity, fontFamily: FONT }}>
      <BuilderBlocks size={size} progress={1} />
      <div style={{ display: "flex", flexDirection: "column", gap: 2 }}>
        <span style={{ fontSize: size * 0.54, fontWeight: 700, color: FG, letterSpacing: "-0.01em", lineHeight: 1 }}>
          OneMillion
        </span>
        <span style={{ fontSize: size * 0.25, fontWeight: 500, color: MUTED, letterSpacing: "0.18em", textTransform: "uppercase" as const }}>
          Builders
        </span>
      </div>
    </div>
  );
}

// ─── ACT 1: The Problem ───────────────────────────────────────────────
function Act1({ frame }: { frame: number }) {
  const lines = [
    { text: "Every 5 seconds,",                          s: 3,  e: 43,  w: 400, c: MUTED },
    { text: "someone gives up on their idea.",           s: 46, e: 85,  w: 600, c: FG   },
    { text: "Because they couldn't afford to build it.", s: 88, e: 113, w: 400, c: MUTED },
  ];
  return (
    <AbsoluteFill style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", fontFamily: FONT }}>
      {lines.map((l) => {
        const op = show(frame, l.s, l.e, 6, 6);
        const y = interpolate(frame, [l.s, l.s + 12], [18, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
        return (
          <div key={l.text} style={{ opacity: op, transform: `translateY(${y}px)`, textAlign: "center", margin: "3px 0" }}>
            <span style={{ fontSize: 40, fontWeight: l.w, color: l.c, letterSpacing: "-0.025em", lineHeight: 1.3 }}>
              {l.text}
            </span>
          </div>
        );
      })}
    </AbsoluteFill>
  );
}

// ─── ACT 2: The Divide ────────────────────────────────────────────────
function Act2({ frame, fps }: { frame: number; fps: number }) {
  const sc = spring({ frame: Math.max(0, frame - A2.s), fps, from: 1.2, to: 1, config: { damping: 24, stiffness: 80 } });
  const op1 = fi(frame, A2.s, 10) * fo(frame, A2.e, 12);
  const op2 = fi(frame, A2.s + 18, 10) * fo(frame, A2.e, 12);
  return (
    <AbsoluteFill style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", fontFamily: FONT }}>
      <div style={{ transform: `scale(${sc})`, textAlign: "center", lineHeight: 1.02 }}>
        <div style={{ opacity: op1 }}>
          <span style={{ fontSize: 90, fontWeight: 800, color: FG, letterSpacing: "-0.045em", display: "block" }}>
            The AI Divide
          </span>
        </div>
        <div style={{ opacity: op2 }}>
          <span style={{ fontSize: 90, fontWeight: 800, color: FG, letterSpacing: "-0.045em", display: "block" }}>
            is real.
          </span>
        </div>
      </div>
    </AbsoluteFill>
  );
}

// ─── ACT 3: Blocks fly inside the SVG → assemble into logo → quote ────
//
// Blocks animate within the SVG's own coordinate space (viewBox 0 0 32 32,
// overflow:visible). This guarantees zero position mismatch — the blocks
// always land exactly on the logo's block positions because they ARE those
// blocks. Start offsets are in SVG units; positive = right/down, negative = left/up.
//
// SVG sits at approx screen (486, 214) in the 1200×630 canvas.
// scale = 54/32 = 1.6875 px per SVG unit.
// Left canvas edge  →  SVG x = (0   − 486) / 1.6875 = −288
// Right canvas edge →  SVG x = (1200 − 486) / 1.6875 = +423
// Top canvas edge   →  SVG y = (0   − 214) / 1.6875 = −127
// Bottom canvas edge→  SVG y = (630 − 214) / 1.6875 = +246
//
const SVG_LOGO_BLOCKS = [
  { x: 4,  y: 20, a: 1,   sd: 0,  dxStart: -292, dyStart: -147 }, // from top-left
  { x: 18, y: 20, a: 1,   sd: 0,  dxStart:  405, dyStart: -147 }, // from top-right
  { x: 11, y: 10, a: 1,   sd: 7,  dxStart: -299, dyStart:  236 }, // from bottom-left
  { x: 11, y: 0,  a: 0.4, sd: 12, dxStart:  405, dyStart:  246 }, // from bottom-right
];

// Logo rendered with animated block assembly — blocks fly within SVG coordinate space.
function AssemblyLogo({
  frame, fps, assembleStart, size = 54, wordmarkOpacity = 1,
}: {
  frame: number; fps: number; assembleStart: number; size?: number; wordmarkOpacity?: number;
}) {
  const appear = fi(frame, assembleStart, 6);
  return (
    <div style={{ display: "flex", alignItems: "center", gap: 14, fontFamily: FONT }}>
      {/* overflow:visible lets blocks fly outside the 54×54 SVG bounds */}
      <svg width={size} height={size} viewBox="0 0 32 32" fill="none"
        style={{ display: "block", overflow: "visible" }}
      >
        {SVG_LOGO_BLOCKS.map((b, i) => {
          const sp = spring({
            frame: Math.max(0, frame - assembleStart - b.sd),
            fps, from: 0, to: 1,
            config: { damping: 13, stiffness: 75 },
          });
          // Position: springs from start offset to final position
          const rx = b.x + b.dxStart * (1 - sp);
          const ry = b.y + b.dyStart * (1 - sp);
          // Scale: 4× when far, 1× when arrived
          const sc = 1 + 3 * Math.max(0, 1 - Math.min(sp * 1.6, 1));
          const w = 10 * sc;
          const h = 8 * sc;
          return (
            <rect key={i}
              x={rx - (w - 10) / 2}
              y={ry - (h - 8) / 2}
              width={w} height={h} rx={1.5}
              fill={FG}
              opacity={b.a * appear}
            />
          );
        })}
      </svg>
      <div style={{ display: "flex", flexDirection: "column", gap: 2, opacity: wordmarkOpacity }}>
        <span style={{ fontSize: size * 0.54, fontWeight: 700, color: FG, letterSpacing: "-0.01em", lineHeight: 1 }}>
          OneMillion
        </span>
        <span style={{ fontSize: size * 0.25, fontWeight: 500, color: MUTED, letterSpacing: "0.18em", textTransform: "uppercase" as const }}>
          Builders
        </span>
      </div>
    </div>
  );
}

function Act3({ frame, fps }: { frame: number; fps: number }) {
  const assembleStart = A3.s;
  // Wordmark fades in after blocks have settled (~frame +55)
  const wordmarkIn = fi(frame, assembleStart + 55, 18);

  const q1op = show(frame, assembleStart + 68, A3.e - 4, 14, 8);
  const q1y  = interpolate(frame, [assembleStart + 68, assembleStart + 88], [20, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const q2op = show(frame, assembleStart + 84, A3.e - 4, 14, 8);
  const q2y  = interpolate(frame, [assembleStart + 84, assembleStart + 104], [20, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const qAop = show(frame, assembleStart + 105, A3.e - 4, 12, 8);

  return (
    <AbsoluteFill style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", fontFamily: FONT }}>
      {/* Logo with animated block assembly */}
      <div style={{ marginBottom: 48 }}>
        <AssemblyLogo frame={frame} fps={fps} assembleStart={assembleStart} size={54} wordmarkOpacity={wordmarkIn} />
      </div>

      {/* Quote */}
      <div style={{ textAlign: "center", maxWidth: 820, padding: "0 64px" }}>
        <div style={{ opacity: q1op, transform: `translateY(${q1y}px)` }}>
          <span style={{ fontSize: 32, fontWeight: 400, color: FG, letterSpacing: "-0.02em", fontStyle: "italic", lineHeight: 1.5 }}>
            "I refuse to let the AI revolution
          </span>
        </div>
        <div style={{ opacity: q2op, transform: `translateY(${q2y}px)` }}>
          <span style={{ fontSize: 32, fontWeight: 400, color: FG, letterSpacing: "-0.02em", fontStyle: "italic", lineHeight: 1.5 }}>
            leave most of humanity behind."
          </span>
        </div>
        <div style={{ opacity: qAop, marginTop: 22 }}>
          <span style={{ fontSize: 18, color: MUTED }}>— Sid Dixit · Builder #000001</span>
        </div>
      </div>
    </AbsoluteFill>
  );
}

// ─── ACT 4: One million [role] ────────────────────────────────────────
const ROLES = [
  "Engineers.",
  "Product Managers.",
  "Entrepreneurs.",
  "Marketers.",
  "Executive Assistants.",
  "Sales Professionals.",
  "Consultants.",
  "Anyone.",
];

function Act4({ frame }: { frame: number }) {
  const headerOp = fi(frame, A4.s, 14) * fo(frame, A4.e, 14);

  const roleDur = 18;  // frames each role is shown
  const roleGap = 18;  // frames between role starts (same = back-to-back)

  // "No coding experience needed." appears at the end
  const noCodeStart = A4.s + ROLES.length * roleGap + 6;
  const noCodeOp = show(frame, noCodeStart, A4.e, 14, 10);

  return (
    <AbsoluteFill style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", fontFamily: FONT }}>
      <div style={{ opacity: headerOp, textAlign: "center", width: "100%" }}>
        <span style={{
          fontSize: 68,
          fontWeight: 800,
          color: FG,
          letterSpacing: "-0.04em",
          display: "block",
          lineHeight: 1.1,
          marginBottom: 4,
        }}>
          One million
        </span>

        {/* Role cycling — clipping container is wide enough for all roles */}
        <div style={{ position: "relative", height: 80, overflow: "visible" as const }}>
          {ROLES.map((role, i) => {
            const rStart = A4.s + 8 + i * roleGap;
            const rEnd   = rStart + roleDur;
            if (frame < rStart - 2 || frame > rEnd + 2) return null;

            const enterT = Math.max(0, Math.min(1, (frame - rStart) / 5));
            const exitT  = Math.max(0, Math.min(1, (rEnd - frame)  / 5));
            const rOp    = Math.min(enterT, exitT);
            const enterY = (1 - enterT) * 18;
            const exitY  = -(1 - exitT) * 18;
            const rY     = frame < (rStart + rEnd) / 2 ? enterY : exitY;

            return (
              <div key={role} style={{
                position: "absolute", inset: 0,
                display: "flex", alignItems: "center", justifyContent: "center",
                opacity: rOp, transform: `translateY(${rY}px)`,
              }}>
                <span style={{
                  fontSize: 60,
                  fontWeight: 800,
                  color: MUTED,
                  letterSpacing: "-0.035em",
                  lineHeight: 1.1,
                  whiteSpace: "nowrap" as const,
                }}>
                  {role}
                </span>
              </div>
            );
          })}
        </div>

        {/* "No coding experience needed." */}
        <div style={{ opacity: noCodeOp, marginTop: 12 }}>
          <span style={{ fontSize: 22, color: MUTED, letterSpacing: "0.01em" }}>
            No coding experience needed.
          </span>
        </div>
      </div>
    </AbsoluteFill>
  );
}

// ─── ACT 5: 18-Day Journey ────────────────────────────────────────────
const DAYS_LABEL = [
  { day: "Day 1",  label: "Idea",     icon: "💡" },
  { day: "Day 6",  label: "Build",    icon: "⚙️" },
  { day: "Day 12", label: "Ship",     icon: "🚀" },
  { day: "Day 18", label: "Badge",    icon: "✦"  },
];

function Act5({ frame }: { frame: number }) {
  const titleOp = show(frame, A5.s, A5.e, 14, 10);
  const titleY  = interpolate(frame, [A5.s, A5.s + 18], [18, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  // Dots: 18 circles appear sequentially
  const DOT_COUNT = 18;
  const dotAreaStart = A5.s + 20;
  const dotDur = 38; // spread over ~38 frames

  // Milestone cards
  const cardDelay = [0, 12, 24, 36];

  // Badge
  const badgeOp = show(frame, A5.s + 60, A5.e, 14, 10);

  return (
    <AbsoluteFill style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 36, fontFamily: FONT }}>

      {/* Title */}
      <div style={{ opacity: titleOp, transform: `translateY(${titleY}px)`, textAlign: "center" }}>
        <span style={{ fontSize: 42, fontWeight: 700, color: FG, letterSpacing: "-0.03em" }}>
          18 Days. 1 Product. 1 Badge.
        </span>
      </div>

      {/* Dot row */}
      <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
        {Array.from({ length: DOT_COUNT }, (_, i) => {
          const dotT = Math.max(0, Math.min(1, (frame - dotAreaStart) / dotDur));
          const threshold = i / (DOT_COUNT - 1);
          const dotVisible = dotT >= threshold;
          const dotScale = dotVisible
            ? spring({ frame: Math.round((frame - dotAreaStart) * (1 - threshold) * 1.5), fps: 30, from: 0, to: 1, config: { damping: 18, stiffness: 200 } })
            : 0;
          const isLast = i === DOT_COUNT - 1;
          return (
            <div
              key={i}
              style={{
                width: isLast ? 18 : 10,
                height: isLast ? 18 : 10,
                borderRadius: "50%",
                background: isLast ? FG : MUTED,
                opacity: dotVisible ? (isLast ? 1 : 0.5) : 0,
                transform: `scale(${dotScale})`,
                flexShrink: 0,
              }}
            />
          );
        })}
      </div>

      {/* Milestone labels */}
      <div style={{ display: "flex", gap: 48, alignItems: "flex-start", justifyContent: "center" }}>
        {DAYS_LABEL.map((m, i) => {
          const mOp = Math.max(0, Math.min(1, (frame - (A5.s + 18 + cardDelay[i])) / 12));
          const mY  = (1 - mOp) * 16;
          return (
            <div key={m.day} style={{
              opacity: mOp, transform: `translateY(${mY}px)`,
              textAlign: "center", display: "flex", flexDirection: "column", gap: 4,
            }}>
              <span style={{ fontSize: 24, lineHeight: 1 }}>{m.icon}</span>
              <span style={{ fontSize: 14, fontWeight: 600, color: FG }}>{m.day}</span>
              <span style={{ fontSize: 13, color: MUTED }}>{m.label}</span>
            </div>
          );
        })}
      </div>

      {/* Badge */}
      <div style={{
        opacity: badgeOp,
        display: "flex", alignItems: "center", gap: 12,
        border: `1px solid ${BORDER}`, borderRadius: 10, padding: "14px 28px",
        background: SURFACE,
      }}>
        <BuilderBlocks size={28} progress={1} />
        <div style={{ display: "flex", flexDirection: "column", gap: 1 }}>
          <span style={{ fontSize: 11, fontWeight: 500, color: MUTED, letterSpacing: "0.15em", textTransform: "uppercase" as const }}>
            Builder
          </span>
          <span style={{ fontSize: 22, fontWeight: 700, color: FG, letterSpacing: "-0.02em", fontVariantNumeric: "tabular-nums" }}>
            #000001
          </span>
        </div>
      </div>

    </AbsoluteFill>
  );
}

// ─── ACT 6: The Counter ───────────────────────────────────────────────
function Act6({ frame, fps }: { frame: number; fps: number }) {
  const tagOp = show(frame, A6.s, A6.s + 50, 14, 8);
  const tagY  = interpolate(frame, [A6.s, A6.s + 18], [18, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  const cStart = A6.s + 24;       // after tagline settles
  const cEnd   = A6.e - 8;        // hold on 1,000,000 for last 8 frames
  const rawT   = Math.max(0, Math.min(1, (frame - cStart) / (cEnd - cStart)));
  // Ease in-out: starts slow (1, 2, 3...), accelerates, slows near 1M
  const eased  = rawT < 0.5
    ? 2 * rawT * rawT
    : 1 - Math.pow(-2 * rawT + 2, 2) / 2;
  const count  = Math.max(1, Math.round(1 + eased * 999_999)); // 1 → 1,000,000

  const cOp = fi(frame, cStart, 14);
  const cSc = spring({ frame: Math.max(0, frame - cStart + 8), fps, from: 0.8, to: 1, config: { damping: 18, stiffness: 100 } });

  return (
    <AbsoluteFill style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 22, fontFamily: FONT }}>
      <div style={{ opacity: tagOp, transform: `translateY(${tagY}px)`, textAlign: "center" }}>
        <span style={{ fontSize: 36, fontWeight: 500, color: MUTED, letterSpacing: "-0.02em" }}>
          The million starts with one.
        </span>
      </div>
      <div style={{ opacity: cOp, transform: `scale(${cSc})`, textAlign: "center" }}>
        <span style={{
          fontSize: 108,
          fontWeight: 800,
          color: FG,
          letterSpacing: "-0.045em",
          fontVariantNumeric: "tabular-nums",
          lineHeight: 1,
        }}>
          {count.toLocaleString()}
        </span>
      </div>
    </AbsoluteFill>
  );
}

// ─── ACT 7: CTA + Final lockup ────────────────────────────────────────
// Words hold for 14f each (was 7) — feels intentional, not rushed
const CTA_WORDS = ["Build.", "Learn.", "Teach.", "Ship."];
const CTA_WORD_DUR = 14;   // frames each word is fully visible
const CTA_WORD_GAP = 16;   // frames between word starts (2f overlap on transitions)

function Act7({ frame }: { frame: number }) {
  // Compute active word
  let activeWord: { text: string; op: number; y: number } | null = null;
  for (let i = 0; i < CTA_WORDS.length; i++) {
    const ws = A7.s + i * CTA_WORD_GAP;
    const we = ws + CTA_WORD_DUR;
    if (frame >= ws - 1 && frame <= we + 3) {
      const eO = Math.max(0, Math.min(1, (frame - ws) / 6));
      const xO = Math.max(0, Math.min(1, (we - frame) / 6));
      const op = Math.min(eO, xO);
      if (op > 0) activeWord = { text: CTA_WORDS[i], op, y: (1 - eO) * 14 };
    }
  }

  // Final brand lockup — appears after flash words settle
  const lockupStart = A7.s + CTA_WORDS.length * CTA_WORD_GAP + 10;
  const lockupOp    = fi(frame, lockupStart, 18);
  const lockupY     = interpolate(frame, [lockupStart, lockupStart + 20], [18, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });

  return (
    <AbsoluteFill style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", fontFamily: FONT }}>
      {/* Flash words */}
      {activeWord && (
        <div style={{ position: "absolute", inset: 0, display: "flex", alignItems: "center", justifyContent: "center" }}>
          <span style={{
            fontSize: 64, fontWeight: 800, color: FG, letterSpacing: "-0.04em",
            opacity: activeWord.op,
            transform: `translateY(${activeWord.y}px)`,
          }}>
            {activeWord.text}
          </span>
        </div>
      )}

      {/* Final lockup: Logo → "Join the Movement." → URL */}
      <div style={{
        opacity: lockupOp,
        transform: `translateY(${lockupY}px)`,
        textAlign: "center",
        display: "flex", flexDirection: "column", alignItems: "center", gap: 24,
      }}>
        <BuilderBlocks size={64} progress={1} />
        <span style={{ fontSize: 40, fontWeight: 700, color: FG, letterSpacing: "-0.03em" }}>
          Join the Movement.
        </span>
        <span style={{ fontSize: 16, color: MUTED, letterSpacing: "0.05em" }}>
          www.onemillion.build
        </span>
      </div>
    </AbsoluteFill>
  );
}

// ─── Root Composition ─────────────────────────────────────────────────
export function GitHubHero() {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill style={{ background: BG, overflow: "hidden" }}>
      {frame <= A1.e + 6                          && <Act1 frame={frame} />}
      {frame >= A2.s - 4 && frame <= A2.e + 6    && <Act2 frame={frame} fps={fps} />}
      {frame >= A3.s - 4 && frame <= A3.e + 6    && <Act3 frame={frame} fps={fps} />}
      {frame >= A4.s - 4 && frame <= A4.e + 6    && <Act4 frame={frame} />}
      {frame >= A5.s - 4 && frame <= A5.e + 6    && <Act5 frame={frame} />}
      {frame >= A6.s - 4 && frame <= A6.e + 6    && <Act6 frame={frame} fps={fps} />}
      {frame >= A7.s - 4                          && <Act7 frame={frame} />}
      <div style={{ position: "absolute", bottom: 0, left: 0, right: 0, height: 1, background: BORDER }} />
    </AbsoluteFill>
  );
}
