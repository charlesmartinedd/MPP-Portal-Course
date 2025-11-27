# MPP Portal Interactive Scroll - Articulate Rise Deployment Guide

## Quick Start (5 Minutes)

### Step 1: Get the HTML File
The complete files are ready at:
```
MPP-Portal-Course/index.html                        (for Rise direct upload)
MPP-Portal-Course/mpp-portal-scroll-complete.html   (alternative/backup)
```

**File Details:**
- Size: 5.55 MB
- All assets embedded (no external files needed)
- Optimized for Articulate Rise

### Step 2: Deploy to Articulate Rise

**Method 1: Direct Upload (Recommended for Rise)**
1. Use the `index.html` file for Rise's home page requirement
2. Upload as the main course file

**Method 2: Code Block Embed**

1. **Log in to Articulate Rise**
   - Go to https://rise.articulate.com
   - Open your course

2. **Add a Code Block**
   - Click "+ Add Block"
   - Select "Embed" from the options
   - Choose "Code"

3. **Paste the HTML**
   - Open `mpp-portal-scroll-complete.html` in a text editor
   - Select All (Ctrl+A) and Copy (Ctrl+C)
   - Paste into the Rise Code Block

4. **Configure the Block**
   - Set height: **750px** (recommended)
   - Click "Preview" to test
   - Adjust height if needed (600px for compact, 800px for spacious)

5. **Test the Interaction**
   - Click the "Start Tour" button
   - Verify smooth scrolling (50 seconds)
   - Check that indicators appear at: 3s, 10s, 22s, 35s, 45s
   - Confirm audio plays (may need to click due to browser autoplay policies)
   - Verify "Restart Tour" button appears at the end

### Step 3: Publish

1. Click "Publish" in Rise
2. Test in published output
3. Verify on different devices (desktop, tablet, mobile)

---

## Interaction Features

### User Experience Flow

1. **Initial State**
   - Elegant modal with "Start Tour" button
   - DoD blue gradient background
   - Clear call-to-action

2. **During Scroll (50 seconds)**
   - Smooth automatic scrolling from top to bottom
   - AI voiceover narration
   - 5 visual indicators pointing to key features:
     - 3s: JOIN NOW button
     - 10s: Subcontracting pool icon
     - 22s: Technical education icon
     - 35s: MPP Summit logo
     - 45s: Contact form

3. **Completion**
   - Small "Restart Tour" button appears at bottom
   - Click to replay from the beginning

### Keyboard Navigation

- **Enter/Space**: Start tour (when not running)
- **Escape**: Restart tour (returns to initial state)
- **Tab**: Navigate to interactive elements

### Accessibility Features

- WCAG 2.1 AA compliant
- ARIA labels for screen readers
- Keyboard navigation support
- Focus indicators
- Alt text for image content
- Live region announcements

---

## Customization Options

### Adjusting Block Height

Recommended heights by use case:

| Use Case | Height | Notes |
|----------|--------|-------|
| **Standard** | 750px | Best for most courses |
| **Compact** | 600px | Space-constrained lessons |
| **Spacious** | 800-900px | Feature highlight |
| **Mobile-first** | 400-500px | Mobile-optimized courses |

### Responsive Behavior

The interaction automatically adapts to screen size:
- **Mobile (≤768px)**: 350px viewport height
- **Tablet (769-1024px)**: 600px viewport height
- **Desktop (≥1025px)**: 700px viewport height

---

## Troubleshooting

### Audio Not Playing

**Cause**: Browser autoplay restrictions

**Solution**:
- Audio requires user interaction (the button click satisfies this)
- If still not working, check browser console for errors
- Ensure Rise doesn't override audio settings

**Workaround**:
- Add instruction text: "Click Start Tour (audio will play)"
- Test in different browsers

### Visual Indicators Not Showing

**Check**:
1. Are you viewing in Rise preview or published output?
2. Is JavaScript enabled?
3. Check browser console for errors

### Scroll Animation Choppy

**Causes**:
- Large file size
- Browser performance
- Rise iframe rendering

**Solutions**:
- Clear browser cache
- Test in Chrome (best performance)
- Ensure Rise block height is set correctly

### Interaction Not Responsive

**Check**:
- Rise block height setting
- Viewport meta tags (should be automatic)
- Test on actual device vs browser simulator

---

## Technical Specifications

### File Structure
```
mpp-portal-scroll-complete.html (5.55 MB)
├── HTML Structure
├── Inline CSS (~15 KB)
│   ├── DoD Branding
│   ├── Responsive Breakpoints
│   └── Animation Keyframes
├── Inline JavaScript (~20 KB)
│   ├── PortalScrollExperience Class
│   ├── Animation Engine
│   └── Event Handlers
├── Embedded Image (Base64)
│   └── cover-page-optimized.png (5.27 MB)
└── Embedded Audio (Base64)
    └── mpp-portal-voiceover.mp3 (264 KB)
```

### Browser Support

| Browser | Version | Status | Notes |
|---------|---------|--------|-------|
| Chrome | 90+ | ✅ Full | Recommended |
| Firefox | 88+ | ✅ Full | Tested |
| Safari | 14+ | ✅ Full | iOS Safari important |
| Edge | 90+ | ✅ Full | Chromium-based |

### Performance Targets

- First Paint: < 1.5s
- Interactive: < 2.5s
- Animation: 60fps sustained
- Memory: < 150MB
- File Size: 5.55 MB (acceptable for modern bandwidth)

---

## Testing Checklist

Before publishing, verify:

- [ ] Play button appears centered
- [ ] Button click starts tour
- [ ] Audio plays (or instructions shown if blocked)
- [ ] Scroll animation smooth (50 seconds)
- [ ] 5 indicators appear at correct times
- [ ] Indicators fade in/out properly
- [ ] Restart button appears at end
- [ ] Restart button resets to initial state
- [ ] Keyboard navigation works
- [ ] Mobile responsive (test on real device)
- [ ] Tablet responsive
- [ ] Desktop responsive
- [ ] Screen reader announces tour status

---

## Alternative Deployment Methods

### Method 1: Code Block (Recommended) ✅
**Pros**: Easy, no external hosting needed
**Cons**: Large file size in Rise project
**Best for**: Single course deployment

### Method 2: Hosted iFrame
**Process**:
1. Upload HTML to web server or CDN
2. Use Rise Embed > URL option
3. Point to hosted file

**Pros**: Smaller Rise project, easier updates
**Cons**: Requires external hosting
**Best for**: Multiple course deployments

### Method 3: SCORM Package
**Process**:
1. Package HTML as standalone SCORM module
2. Import into Rise as external link

**Pros**: Tracking capabilities
**Cons**: More complex setup
**Best for**: LMS integration with tracking

---

## Support Resources

### Documentation Files
- `README.md` - Project overview
- `DEPLOYMENT-GUIDE.md` - This file
- `.claude/plans/elegant-wishing-shell.md` - Complete implementation plan

### Source Files
- `src/mpp-portal-scroll.html` - Template (before asset embedding)
- `assets/cover-page-optimized.png` - Optimized image (3.96 MB)
- `assets/mpp-portal-voiceover.mp3` - AI-generated audio (198 KB)
- `assets/voiceover-script.txt` - Narration script

### Generation Scripts
- `assets/optimize_image.py` - Image compression
- `assets/generate_voiceover.py` - AI voiceover generation
- `assets/embed_assets.py` - Base64 embedding

---

## Updates and Modifications

### To Update the Image:
1. Replace `Cover Page.png` with new image
2. Run: `python assets/optimize_image.py`
3. Run: `python assets/embed_assets.py`
4. Copy new HTML to Rise

### To Update the Voiceover:
1. Edit script in `assets/generate_voiceover.py`
2. Run: `python assets/generate_voiceover.py`
3. Run: `python assets/embed_assets.py`
4. Copy new HTML to Rise

### To Adjust Timing:
1. Edit `CONFIG.totalDuration` in `src/mpp-portal-scroll.html`
2. Update indicator times in `CONFIG.indicators`
3. Run: `python assets/embed_assets.py`
4. Copy new HTML to Rise

---

## Questions?

For technical support or customization requests:
- Review the complete plan: `.claude/plans/elegant-wishing-shell.md`
- Check project documentation in `docs/`
- Test locally by opening `mpp-portal-scroll-complete.html` in browser

---

**Created**: November 27, 2025
**Version**: 1.0
**Project**: MPP Portal Interactive Scroll Experience
