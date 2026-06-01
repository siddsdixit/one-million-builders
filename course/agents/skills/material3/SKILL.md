# Material Design 3 — Design System Reference

> Core M3 reference for the Design and Build agents. For live queries (component code, full icon search, accessibility details), use the `material3` MCP server tools. This skill provides the essential tokens and patterns for offline/fast access.

---

## MCP Server (preferred for deep queries)

If the `material3` MCP server is available, use these tools:
- `list_material_components` — browse components by category
- `get_component_code` — get real implementation code
- `get_design_tokens` — export tokens as CSS/SCSS/JSON/JS
- `search_material_icons` — search 2,500+ Material Symbols icons
- `get_accessibility_guidelines` — WCAG 2.1 compliance per component

## Dynamic Color System

M3's color system generates a full palette from ONE seed color.

### How It Works
1. Builder picks a seed color (e.g., `#C17952` terracotta)
2. M3 algorithm generates 5 tonal palettes (primary, secondary, tertiary, neutral, neutral-variant)
3. Each palette has 13 tones (0, 10, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 95, 98, 99, 100)
4. Light and dark themes pick specific tones from these palettes

### Color Roles (map these to CSS custom properties)

**Light Theme:**
```css
:root {
  /* Primary */
  --md-sys-color-primary: /* tone 40 from primary palette */;
  --md-sys-color-on-primary: /* tone 100 */;
  --md-sys-color-primary-container: /* tone 90 */;
  --md-sys-color-on-primary-container: /* tone 10 */;

  /* Secondary */
  --md-sys-color-secondary: /* tone 40 from secondary palette */;
  --md-sys-color-on-secondary: /* tone 100 */;
  --md-sys-color-secondary-container: /* tone 90 */;
  --md-sys-color-on-secondary-container: /* tone 10 */;

  /* Tertiary */
  --md-sys-color-tertiary: /* tone 40 from tertiary palette */;
  --md-sys-color-on-tertiary: /* tone 100 */;
  --md-sys-color-tertiary-container: /* tone 90 */;
  --md-sys-color-on-tertiary-container: /* tone 10 */;

  /* Error */
  --md-sys-color-error: #BA1A1A;
  --md-sys-color-on-error: #FFFFFF;
  --md-sys-color-error-container: #FFDAD6;
  --md-sys-color-on-error-container: #410002;

  /* Surface (5 levels) */
  --md-sys-color-surface: /* tone 98 from neutral */;
  --md-sys-color-on-surface: /* tone 10 from neutral */;
  --md-sys-color-surface-variant: /* tone 90 from neutral-variant */;
  --md-sys-color-on-surface-variant: /* tone 30 from neutral-variant */;
  --md-sys-color-surface-container-lowest: /* tone 100 */;
  --md-sys-color-surface-container-low: /* tone 96 */;
  --md-sys-color-surface-container: /* tone 94 */;
  --md-sys-color-surface-container-high: /* tone 92 */;
  --md-sys-color-surface-container-highest: /* tone 90 */;

  /* Outline */
  --md-sys-color-outline: /* tone 50 from neutral-variant */;
  --md-sys-color-outline-variant: /* tone 80 from neutral-variant */;
}
```

**Dark Theme — swap tones:**
```css
[data-theme="dark"] {
  --md-sys-color-primary: /* tone 80 */;
  --md-sys-color-on-primary: /* tone 20 */;
  --md-sys-color-primary-container: /* tone 30 */;
  --md-sys-color-on-primary-container: /* tone 90 */;
  --md-sys-color-surface: /* tone 6 */;
  --md-sys-color-on-surface: /* tone 90 */;
  /* ... same pattern for all roles */
}
```

## Typography Scale

M3 defines 15 named styles across 5 roles:

| Role | Large | Medium | Small |
|------|-------|--------|-------|
| **Display** | 57/64 regular | 45/52 regular | 36/44 regular |
| **Headline** | 32/40 regular | 28/36 regular | 24/32 regular |
| **Title** | 22/28 medium | 16/24 medium | 14/20 medium |
| **Body** | 16/24 regular | 14/20 regular | 12/16 regular |
| **Label** | 14/20 medium | 12/16 medium | 11/16 medium |

Format: `font-size/line-height weight`

### Font Recommendations
- **Display/Headline:** Use a distinctive font (DM Serif Display, Playfair, Space Grotesk)
- **Body/Label:** Roboto (M3 default) or Plus Jakarta Sans, Inter, Satoshi

## Shape System

| Token | Value | Use |
|-------|-------|-----|
| `--md-sys-shape-corner-none` | 0px | — |
| `--md-sys-shape-corner-extra-small` | 4px | Chips, small elements |
| `--md-sys-shape-corner-small` | 8px | Buttons, text fields |
| `--md-sys-shape-corner-medium` | 12px | Cards, dialogs |
| `--md-sys-shape-corner-large` | 16px | FAB, large cards |
| `--md-sys-shape-corner-extra-large` | 28px | Sheets, bottom sheets |
| `--md-sys-shape-corner-full` | 9999px | Pills, avatars |

## Elevation System

| Level | Shadow | Use |
|-------|--------|-----|
| 0 | none | Flat surfaces |
| 1 | `0 1px 2px rgba(0,0,0,0.1), 0 1px 3px rgba(0,0,0,0.08)` | Cards, app bar |
| 2 | `0 2px 4px rgba(0,0,0,0.1), 0 1px 6px rgba(0,0,0,0.08)` | Raised elements |
| 3 | `0 4px 8px rgba(0,0,0,0.12), 0 2px 4px rgba(0,0,0,0.08)` | FAB, dialogs |
| 4 | `0 6px 12px rgba(0,0,0,0.14), 0 3px 6px rgba(0,0,0,0.1)` | Navigation drawer |
| 5 | `0 8px 16px rgba(0,0,0,0.16), 0 4px 8px rgba(0,0,0,0.12)` | Modals |

## Motion System

| Token | Value | Use |
|-------|-------|-----|
| `--md-sys-motion-duration-short1` | 50ms | Micro-interactions |
| `--md-sys-motion-duration-short2` | 100ms | Ripple |
| `--md-sys-motion-duration-short3` | 150ms | Button press, hover |
| `--md-sys-motion-duration-short4` | 200ms | Chip, switch toggle |
| `--md-sys-motion-duration-medium1` | 250ms | Card expand |
| `--md-sys-motion-duration-medium2` | 300ms | Dialog, sheet |
| `--md-sys-motion-duration-medium3` | 350ms | Navigation transition |
| `--md-sys-motion-duration-medium4` | 400ms | Page transition |
| `--md-sys-motion-duration-long1` | 450ms | Complex animations |
| `--md-sys-motion-duration-long2` | 500ms | Full page morph |
| `--md-sys-motion-easing-standard` | `cubic-bezier(0.2, 0, 0, 1)` | Most transitions |
| `--md-sys-motion-easing-emphasized` | `cubic-bezier(0.2, 0, 0, 1)` | Enter/exit |
| `--md-sys-motion-easing-emphasized-decelerate` | `cubic-bezier(0.05, 0.7, 0.1, 1)` | Enter |
| `--md-sys-motion-easing-emphasized-accelerate` | `cubic-bezier(0.3, 0, 0.8, 0.15)` | Exit |

## Core Components (Top 20)

### Navigation
| Component | Use | Key Tokens |
|-----------|-----|------------|
| Top app bar | Page header with title + actions | surface-container, elevation 0-2 |
| Navigation bar | Mobile bottom nav (3-5 destinations) | surface-container, secondary-container for active |
| Navigation rail | Tablet sidebar (icons + labels, 56-80px wide) | surface-container |
| Navigation drawer | Desktop sidebar (280px, labels + icons + sections) | surface-container-low |
| Bottom sheet | Modal/persistent overlay from bottom | surface-container-low, corner-extra-large top |

### Actions
| Component | Use | Key Tokens |
|-----------|-----|------------|
| Filled button | Primary CTA | primary, on-primary, corner-full |
| Outlined button | Secondary action | outline border, primary text |
| Text button | Tertiary/cancel | primary text, no border |
| FAB | Primary floating action | primary-container, corner-large, elevation 3 |
| Icon button | Toolbar actions | on-surface-variant, 40x40 touch target |

### Containers
| Component | Use | Key Tokens |
|-----------|-----|------------|
| Card (filled) | Content container | surface-container-low, corner-medium |
| Card (elevated) | Emphasized content | surface-container-low, elevation 1, corner-medium |
| Card (outlined) | Distinct boundary | outline-variant border, corner-medium |
| Dialog | Modal decisions | surface-container-high, corner-extra-large, elevation 3 |

### Selection
| Component | Use | Key Tokens |
|-----------|-----|------------|
| Chip (filter) | Filter/toggle | outline border → secondary-container when active |
| Chip (assist) | Smart suggestions | outline border, corner-small |
| Checkbox | Multi-select | primary when checked |
| Switch | On/off toggle | primary when on, surface-variant when off |

### Input
| Component | Use | Key Tokens |
|-----------|-----|------------|
| Text field (filled) | Primary input | surface-container-highest, corner-extra-small top |
| Text field (outlined) | Alternative input | outline border, corner-extra-small |
| Search bar | Global search | surface-container-high, corner-full |

### Feedback
| Component | Use | Key Tokens |
|-----------|-----|------------|
| Snackbar | Brief notification | inverse-surface, inverse-on-surface, corner-extra-small |
| Progress indicator | Loading state | primary on surface-container-highest |
| Badge | Count/status | error for dot, error-container for number |

## Responsive Layout Grid

| Breakpoint | Columns | Margin | Gutter | Navigation |
|------------|---------|--------|--------|------------|
| Compact (< 600px) | 4 | 16px | 8px | Bottom nav bar |
| Medium (600-840px) | 8 | 24px | 16px | Navigation rail |
| Expanded (> 840px) | 12 | 24px | 24px | Navigation drawer |

### Max Content Width
- **1280px** centered on expanded breakpoint
- Cards: max-width 360px in grids

## Icon Library

Use **Material Symbols Outlined** (not Material Icons — those are legacy).

```html
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" rel="stylesheet">
```

Common icons for apps:
- Navigation: `home`, `explore`, `search`, `menu`, `arrow_back`, `close`
- Actions: `edit`, `delete`, `share`, `bookmark`, `favorite`, `add`
- Content: `image`, `description`, `calendar_today`, `schedule`, `person`
- Status: `check_circle`, `error`, `warning`, `info`, `notifications`
- Commerce: `shopping_cart`, `payments`, `receipt`

## React Implementation (MUI)

For the build agent — use MUI v6+ which implements M3:

```bash
npm install @mui/material @emotion/react @emotion/styled @mui/icons-material
```

### Theme Setup
```tsx
import { createTheme, ThemeProvider } from '@mui/material/styles';

const theme = createTheme({
  colorSchemes: {
    light: {
      palette: {
        primary: { main: '#8B4513' }, // seed color
      },
    },
    dark: true, // auto-generates dark palette from seed
  },
  shape: { borderRadius: 12 }, // M3 medium
  typography: {
    fontFamily: '"Plus Jakarta Sans", sans-serif',
    h1: { fontFamily: '"DM Serif Display", serif' },
    h2: { fontFamily: '"DM Serif Display", serif' },
    h3: { fontFamily: '"DM Serif Display", serif' },
  },
});
```

MUI maps M3 tokens automatically. Use `<Button variant="contained">`, `<Card>`, `<TextField>`, `<AppBar>`, `<BottomNavigation>`, etc.

## Component Code Snippets (self-contained — no MCP needed)

### Top App Bar
```tsx
<AppBar position="sticky" color="default" elevation={0}
  sx={{ borderBottom: 1, borderColor: 'divider' }}>
  <Toolbar>
    <Typography variant="h6" sx={{ fontFamily: '"DM Serif Display"', flexGrow: 1 }}>
      {appName}
    </Typography>
    <IconButton><DarkModeOutlined /></IconButton>
    <Avatar src={user.avatar} sx={{ width: 32, height: 32, ml: 1 }} />
  </Toolbar>
</AppBar>
```

### Bottom Navigation
```tsx
<BottomNavigation value={tab} onChange={(_, v) => setTab(v)}
  sx={{ position: 'fixed', bottom: 0, left: 0, right: 0,
        borderTop: 1, borderColor: 'divider' }}>
  <BottomNavigationAction label="Home" icon={<Home />} />
  <BottomNavigationAction label="Explore" icon={<Explore />} />
  <BottomNavigationAction label="Cookbook" icon={<MenuBook />} />
  <BottomNavigationAction label="Profile" icon={<Person />} />
</BottomNavigation>
```

### Navigation Drawer (Desktop)
```tsx
<Drawer variant="permanent" sx={{ width: 280, '& .MuiDrawer-paper': { width: 280 } }}>
  <Typography variant="h5" sx={{ p: 2, fontFamily: '"DM Serif Display"', color: 'primary.main' }}>
    {appName}
  </Typography>
  <List>
    <ListItemButton selected={active === 'home'}>
      <ListItemIcon><Home /></ListItemIcon>
      <ListItemText primary="Home" />
    </ListItemButton>
    {/* ... more items */}
  </List>
</Drawer>
```

### Card (Filled)
```tsx
<Card sx={{ borderRadius: 3, overflow: 'hidden', cursor: 'pointer',
           '&:hover': { boxShadow: 3, transform: 'translateY(-2px)' },
           transition: 'all 0.15s ease' }}>
  <CardMedia component="img" height={180} image={recipe.image} alt={recipe.title} />
  <CardContent>
    <Typography variant="subtitle1" noWrap>{recipe.title}</Typography>
    <Stack direction="row" spacing={1} alignItems="center" mt={0.5}>
      <Avatar src={recipe.author.avatar} sx={{ width: 20, height: 20 }} />
      <Typography variant="caption" color="text.secondary">{recipe.author.name}</Typography>
    </Stack>
    <Stack direction="row" spacing={2} mt={1}>
      <Typography variant="caption" color="text.secondary">
        <FavoriteOutlined sx={{ fontSize: 14, mr: 0.5 }} />{recipe.likes}
      </Typography>
      <Typography variant="caption" color="text.secondary">
        <ScheduleOutlined sx={{ fontSize: 14, mr: 0.5 }} />{recipe.time}
      </Typography>
    </Stack>
  </CardContent>
</Card>
```

### Search Bar
```tsx
<TextField fullWidth placeholder="Search recipes, cooks, or ingredients..."
  variant="outlined"
  sx={{ '& .MuiOutlinedInput-root': {
    borderRadius: 99, backgroundColor: 'action.hover',
    '& fieldset': { border: 'none' }
  }}}
  InputProps={{
    startAdornment: <InputAdornment position="start"><Search /></InputAdornment>,
    endAdornment: <InputAdornment position="end"><TuneOutlined /></InputAdornment>,
  }}
/>
```

### Filter Chips
```tsx
<Stack direction="row" spacing={1} sx={{ overflowX: 'auto', pb: 1 }}>
  {filters.map(f => (
    <Chip key={f} label={f} variant={active === f ? 'filled' : 'outlined'}
      color={active === f ? 'secondary' : 'default'}
      onClick={() => setActive(f)} />
  ))}
</Stack>
```

### FAB
```tsx
<Fab color="primaryContainer" sx={{ position: 'fixed', bottom: 80, right: 16 }}>
  <Edit />
</Fab>
```

### Dialog (Confirmation)
```tsx
<Dialog open={open} onClose={onClose} PaperProps={{ sx: { borderRadius: 7 } }}>
  <DialogTitle>Delete recipe?</DialogTitle>
  <DialogContent>
    <DialogContentText>This action cannot be undone.</DialogContentText>
  </DialogContent>
  <DialogActions>
    <Button onClick={onClose}>Cancel</Button>
    <Button onClick={onDelete} color="error" variant="contained">Delete</Button>
  </DialogActions>
</Dialog>
```

### Snackbar (Toast)
```tsx
<Snackbar open={show} autoHideDuration={5000} onClose={() => setShow(false)}
  anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}>
  <Alert severity="success" variant="filled" sx={{ borderRadius: 2 }}>
    Recipe saved to cookbook!
  </Alert>
</Snackbar>
```

### Responsive Navigation Pattern
```tsx
// In layout.tsx — switches nav based on viewport
const isDesktop = useMediaQuery('(min-width: 841px)');
const isTablet = useMediaQuery('(min-width: 600px) and (max-width: 840px)');

return (
  <Box sx={{ display: 'flex' }}>
    {isDesktop && <NavigationDrawer />}
    {isTablet && <NavigationRail />}
    <Box component="main" sx={{ flexGrow: 1, ml: isDesktop ? '280px' : isTablet ? '80px' : 0 }}>
      {children}
    </Box>
    {!isDesktop && !isTablet && <BottomNavigation />}
  </Box>
);
```

## Extended Icon Reference

### Navigation & UI (100 most used)
`home`, `explore`, `search`, `menu`, `arrow_back`, `arrow_forward`, `close`, `more_vert`, `more_horiz`, `settings`, `tune`, `filter_list`, `sort`, `expand_more`, `expand_less`, `chevron_left`, `chevron_right`, `refresh`, `fullscreen`, `open_in_new`

### Actions
`edit`, `delete`, `add`, `remove`, `save`, `share`, `bookmark`, `bookmark_border`, `favorite`, `favorite_border`, `thumb_up`, `thumb_down`, `reply`, `forward`, `download`, `upload`, `content_copy`, `content_paste`, `undo`, `redo`

### Content & Media
`image`, `photo_camera`, `videocam`, `mic`, `volume_up`, `play_arrow`, `pause`, `stop`, `skip_next`, `skip_previous`, `article`, `description`, `text_snippet`, `link`, `attach_file`, `folder`, `cloud_upload`

### People & Social
`person`, `people`, `group`, `person_add`, `person_remove`, `account_circle`, `face`, `chat`, `forum`, `mail`, `send`, `notifications`, `notifications_active`

### Status & Feedback
`check`, `check_circle`, `done`, `done_all`, `error`, `error_outline`, `warning`, `info`, `help`, `visibility`, `visibility_off`, `lock`, `lock_open`, `verified`

### Time & Calendar
`schedule`, `access_time`, `calendar_today`, `event`, `date_range`, `timer`, `alarm`, `history`, `update`

### Commerce & Finance
`shopping_cart`, `shopping_bag`, `store`, `payments`, `credit_card`, `receipt`, `local_offer`, `sell`, `attach_money`, `account_balance_wallet`

### Data & Files
`dashboard`, `analytics`, `bar_chart`, `pie_chart`, `trending_up`, `trending_down`, `leaderboard`, `insert_chart`, `table_chart`

### Maps & Location
`location_on`, `map`, `navigation`, `directions`, `local_dining`, `restaurant`, `local_cafe`, `local_grocery_store`
