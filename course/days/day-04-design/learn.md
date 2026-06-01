# Day 4 — Design The Product

<p align="center">
  <a href="../../README.md">Course Home</a> &bull;
  <a href="./learn.md">Learn</a> &bull;
  <a href="./build.md">Build</a> &bull;
  <a href="./resources.md">Resources</a> &bull;
  <a href="./loom.md">Video</a>
</p>

**Primary agent:** `design`
**Supporting agents:** validate-spec

Day 4 is where the product becomes visible before anyone writes app code. You take the Day 3 refined PRD and turn it into screens, flows, states, visual language, seed data, and a preview you can approve.

The design agent is not a decorator. It is the pipeline stage that prevents random UI, missing states, and rebuilds later.

## Learning Frame

- **Mental model:** design is product behavior made visible. A screen is not just colors; it is a promise about what the user can do, what happens next, and how the product responds.
- **Input:** `.onemillion/refined-prd.md`
- **Output:** design artifacts the plan and build agents can follow without guessing.
- **What can go wrong:** the harness makes visual choices without teaching them, skips mobile/desktop tradeoffs, forgets loading/empty/error states, or lets the builder approve a design they have not seen.
- **What to ignore today:** do not code the app. Do not set up Vercel or Supabase. Today freezes the experience before architecture and build.

## What You Learn

- turn refined PRD into screens and flows
- explain what good product design means
- decide web app, mobile-first, desktop-first, or hybrid interface priorities
- choose a visual direction based on the user, domain, and emotional tone
- use MUI / Material Design 3 as the course design language
- define layout, navigation, typography, color, icon, motion, and interaction rules
- design loading, empty, error, partial, full, and success states
- create realistic seed data so the app looks alive on first run
- review an HTML mockup before approving the design

## Core Concepts

### Good Design

Good design makes the right action obvious for the right person. It should answer:

- Who is this for?
- What is the user trying to accomplish?
- What does the user see first?
- What action should they take next?
- What happens when there is no data, too much data, slow data, wrong data, or an error?
- What should the product feel like: serious, warm, fast, playful, premium, operational, educational, clinical, creative?

### Design Direction

Before choosing colors or screens, define a one-sentence aesthetic intent. Examples:

- Clean operational dashboard for busy managers who need fast decisions.
- Warm editorial planner for creators who want calm and focus.
- Sharp enterprise console for technical teams managing risk.
- Playful learning workspace for beginners who need confidence and feedback.

This direction drives color, font, density, layout, motion, empty states, and copy tone.

### Audience-Based Design

A product for a teacher, doctor, teenager, founder, warehouse operator, designer, or finance team should not look the same.

- **Enterprise users:** dense layouts, tables, filters, auditability, conservative color, clear hierarchy.
- **Creators/consumers:** richer visuals, cards, imagery, emotion, sharing moments.
- **Beginners:** simple navigation, friendly empty states, fewer controls per screen.
- **Power users:** keyboard-friendly flows, compact density, saved views, bulk actions.
- **Mobile-first audiences:** bottom navigation, thumb-friendly actions, short forms.
- **Desktop-first audiences:** sidebar navigation, tables, split panes, dashboards.

### Web App And Mobile Design

Most OneMillion products are responsive web apps. Day 4 decides how they adapt:

- Mobile should have 44px minimum touch targets, short forms, bottom or simple top navigation, and one primary action per screen.
- Desktop can support sidebars, dashboards, data tables, multi-column layouts, and deeper filtering.
- Tablet often needs a middle layout, not just stretched mobile.
- Content should have a max width; it should not stretch edge-to-edge on ultra-wide screens.

### MUI / Material Design 3

MUI gives this course a shared implementation language for React. The design agent should not invent random components. It should map the experience to MUI patterns:

- Buttons, icon buttons, chips, tabs, cards, dialogs, drawers, forms, lists, tables, skeletons, snackbars, and navigation.
- A theme with a real seed color, typography scale, spacing, radius, shadows, states, and dark mode.
- Accessibility defaults: labels, focus states, contrast, reduced motion, and keyboard navigation.

### Content States

Every important screen must define:

- **Loading:** skeletons that match the layout, not a full-page spinner.
- **Empty:** helpful message and next action.
- **Error:** human-readable problem and retry path.
- **Partial:** what 1-3 records look like.
- **Full:** what the ideal seeded product looks like.
- **Success:** clear feedback after create, update, delete, send, save, or complete.

### Seed Data

An empty app kills momentum. Day 4 should create realistic `.onemillion/seed-data.json` so Day 6-8 can show the product with believable users, records, images, statuses, dates, and relationships.

### Preview Before Build

For a web app or hybrid product, the design agent should generate `.onemillion/mockup/index.html` and serve it locally so you can see the direction before approving. The mockup is not app code. It is a visual contract for the plan and build stages.

## What You Produce

- `.onemillion/design-spec.md`
- `.onemillion/design-system.md`
- `.onemillion/globals.css`
- `.onemillion/screens/`
- `.onemillion/seed-data.json`
- `.onemillion/mockup/index.html` for web app or hybrid products
- `.onemillion/assets/design-spec.pdf` when PDF generation is available

## Human Decisions

- primary user flow
- visual direction
- primary device: mobile, desktop, or responsive web
- seed color and heading font
- content density: compact, comfortable, or spacious
- navigation pattern
- key MUI component choices
- screen priority
- copy tone
- approval or revision after viewing the mockup

## Done Checklist

- [ ] .onemillion/design-spec.md exists
- [ ] .onemillion/design-system.md exists
- [ ] .onemillion/screens/ contains screen specs for the main screens
- [ ] .onemillion/seed-data.json exists and uses realistic data
- [ ] .onemillion/mockup/index.html exists for web app or hybrid products
- [ ] main screens and states are described
- [ ] loading, empty, error, partial, full, and success states are covered
- [ ] mobile and desktop behavior are described
- [ ] MUI / Material Design 3 component patterns are named
- [ ] learner approved the design direction

## Verify Your Day 4

When the checklist is true, ask your harness to run the OneMillion verifier for Day 4. The verifier should inspect the design artifacts, screen specs, seed data, mockup, and manual approval. There is no deployment gate today.


---

-> **Next:** [Day 5 — Plan Architecture](../day-05-plan-architecture/learn.md)
