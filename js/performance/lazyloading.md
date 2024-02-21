# Lazy Loading

- Load non-critical resources (eg. offscreen elements) only when needed to reduce critical rendering path time.
- Generally on user interactions (eg. scrolling, navigating)
- Example: Landing on homepage and showing link to a cart, but not loading the cart page's resources until navigated to

## Strategies

### Code splitting
- Split JS, CSS, HTML into smaller chunks

### JS script type module
Script tags with `type="module"` are treated as JS modules and deferred by default.

### CSS / Fonts / Images
- by default, CSS is a render-blocking resources, so keep it thin and use media types/queries to unblock rendering
- by default, font requests are delayed until render tree is constructed, so consider preloading web fonts
- Use `loading` attribute on `<img>`, `<iframe>` elements to defer loading of offscreen elements to only when user scrolls near them.

## Precautions when lazy loading

- what's above the fold may be different on different devices
- lazy loading can cause shifts in layouts if placeholders aren't used
- use `width` and `height` attributes on images/video to ensure smooth transitions from placeholders to final images
- consider having a backup plan if lazy loading fails