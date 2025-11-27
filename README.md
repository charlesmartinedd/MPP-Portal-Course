# MPP Portal Interactive Scroll Experience

An immersive, accessible scrolling interaction for Articulate Rise featuring the Mentor-Protégé Program Portal website.

## 📦 What's Included

A complete, single-file HTML experience that simulates browsing the MPP Portal website with:
- **50-second automated scroll** through the entire portal page
- **AI-generated voiceover** narrating key program benefits
- **5 visual indicators** highlighting important UI elements
- **Elegant Play/Restart controls** for learner interaction
- **Full accessibility** (WCAG 2.1 AA compliant)
- **Responsive design** (mobile, tablet, desktop)

## 🚀 Quick Start

### For Articulate Rise Deployment (Recommended)

1. **Download the zip file:**
   ```
   MPP-Portal-Scroll-for-Rise.zip (4.2 MB)
   ```

2. **Upload to Articulate Rise:**
   - Log in to https://rise.articulate.com
   - Click "Upload" or "Import"
   - Select the zip file
   - Rise will automatically detect `index.html`

3. **Test and publish!**

### Alternative: Code Block Embed

For embedding in an existing Rise course:

1. **Open the complete file:**
   ```
   mpp-portal-scroll-complete.html (5.55 MB)
   ```

2. **Copy the entire contents** (Ctrl+A, Ctrl+C)

3. **In Articulate Rise:**
   - Click "+ Add Block"
   - Select "Embed" → "Code"
   - Paste the HTML
   - Set height: **750px**
   - Preview and publish!

**📖 Full deployment guide:** See `docs/DEPLOYMENT-GUIDE.md`

## 🎯 Features

### User Experience
- **Elegant modal** with centered "Start Tour" button
- **Smooth auto-scroll** (50 seconds, 60fps animation)
- **AI voiceover** explaining program benefits
- **Visual indicators** pointing to:
  - JOIN NOW button (3s)
  - Subcontracting pool icon (10s)
  - Technical education icon (22s)
  - MPP Summit logo (35s)
  - Contact form (45s)
- **Small Restart button** appears at completion

### Technical Highlights
- Single 5.55 MB file (no external dependencies)
- All assets embedded as Base64 (image + audio)
- requestAnimationFrame for smooth 60fps animation
- Cubic easing for natural motion
- DoD branding (blue gradient #1e3a5f to #2a5082)
- Keyboard navigation (Enter, Space, Escape, Tab)
- ARIA labels for screen readers

## 📁 Project Structure

```
MPP-Portal-Course/
├── MPP-Portal-Scroll-for-Rise.zip     # 🎯 PRIMARY FILE - Upload this to Rise
├── index.html                          # Contained in zip (5.55 MB)
├── mpp-portal-scroll-complete.html    # Alternative - For Code Block embed
├── Cover Page.png                      # Original source image (8.24 MB)
├── README.md                           # This file
├── TESTING-RESULTS.md                  # Testing checklist and results
├── src/
│   └── mpp-portal-scroll.html         # Template (before asset embedding)
├── assets/
│   ├── cover-page-optimized.png       # Optimized image (3.96 MB, 52% reduction)
│   ├── mpp-portal-voiceover.mp3       # AI voiceover (198.6 KB, 50 seconds)
│   ├── voiceover-script.txt           # Narration script
│   ├── optimize_image.py              # Image compression script
│   ├── generate_voiceover.py          # AI voiceover generation
│   └── embed_assets.py                # Base64 embedding script
├── docs/
│   └── DEPLOYMENT-GUIDE.md            # Comprehensive deployment guide
└── .claude/
    └── plans/
        └── elegant-wishing-shell.md   # Complete implementation plan
```

## 🛠️ Customization

### Update the Image
```bash
# Replace "Cover Page.png" with new image, then:
cd assets
python optimize_image.py
python embed_assets.py
# New mpp-portal-scroll-complete.html will be generated
```

### Update the Voiceover
```bash
# Edit script in assets/generate_voiceover.py, then:
cd assets
python generate_voiceover.py
python embed_assets.py
```

### Adjust Timing
Edit `CONFIG.totalDuration` and `CONFIG.indicators` in `src/mpp-portal-scroll.html`, then re-embed assets.

## 🧪 Testing

### Browser Testing
```bash
# Open in default browser
start mpp-portal-scroll-complete.html
```

### Testing Checklist
See `TESTING-RESULTS.md` for comprehensive testing checklist including:
- Initial state verification
- Button interactions
- Audio playback
- Scroll animation smoothness
- Visual indicator timing
- Restart functionality
- Keyboard navigation
- Accessibility compliance
- Responsive behavior

## 📊 Technical Specifications

| Specification | Value |
|---------------|-------|
| **Total File Size** | 5.55 MB |
| **Image Size** | 3.96 MB (optimized from 8.24 MB) |
| **Audio Size** | 198.6 KB |
| **Code Size** | ~35 KB (HTML + CSS + JavaScript) |
| **Animation Duration** | 50 seconds |
| **Target FPS** | 60fps |
| **Browser Support** | Chrome 90+, Firefox 88+, Safari 14+, Edge 90+ |

## ♿ Accessibility

- **WCAG 2.1 AA Compliant**
- ARIA labels for all interactive elements
- Live region announcements for screen readers
- Full keyboard navigation support
- Focus indicators on all controls
- Alt text for image content

## 🎨 Voiceover Script (82 words, 50 seconds)

> Welcome to the Mentor-Protégé Program Portal — your gateway to transformative defense contracting partnerships.
>
> Mentors shape careers through subcontracting partnerships, networking opportunities, and earning credit toward small business goals.
>
> Protégés receive guidance from prime contractors in business development, technical capabilities, and federal procurement with hands-on support.
>
> Join the annual MPP Summit where mentors and protégés connect to build relationships and discover new collaboration opportunities.
>
> Ready to get connected? Submit your information and our Program Office will guide you through the next steps.

## 📝 Requirements

### For Asset Generation (Optional)
Only needed if regenerating from source:

```bash
pip install pillow edge-tts
```

### For Deployment
- Articulate Rise account
- Modern web browser
- No other dependencies (all-in-one file)

## 🐛 Troubleshooting

### Audio Not Playing
- Audio requires user interaction (button click satisfies this)
- Check browser console for errors
- Verify Articulate Rise doesn't block audio

### Choppy Animation
- Clear browser cache
- Use Chrome for best performance
- Ensure Rise block height is set correctly (750px)

### Indicators Not Showing
- Check JavaScript is enabled
- View browser console for errors
- Test in published output (not just preview)

See `docs/DEPLOYMENT-GUIDE.md` for comprehensive troubleshooting.

## 📚 Documentation

- **Deployment Guide:** `docs/DEPLOYMENT-GUIDE.md` - Step-by-step Rise deployment
- **Implementation Plan:** `.claude/plans/elegant-wishing-shell.md` - Technical specifications
- **Testing Results:** `TESTING-RESULTS.md` - Testing checklist and outcomes

## 📄 License

Created for Department of Defense Mentor-Protégé Program educational content.

## 🙋 Support

For technical support or customization:
1. Review `docs/DEPLOYMENT-GUIDE.md`
2. Test locally: `start mpp-portal-scroll-complete.html`
3. Check browser console for errors
4. Verify asset embedding with `python assets/embed_assets.py`

---

**Created:** November 27, 2025
**Version:** 1.0
**Status:** ✅ Production Ready

**File to Deploy:** `mpp-portal-scroll-complete.html` (5.55 MB)
