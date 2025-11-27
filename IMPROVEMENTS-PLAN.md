# MPP Portal Interactive Scroll - Improvements Plan

**Date:** November 27, 2025
**Based on:** Articulate Rise testing feedback

---

## 📋 Issues to Address

### 1. Gray Space Around Image ❌
**Problem:** Image not filling viewport width, leaving gray space on sides
**Current:** Image has `max-width: 800px` constraint
**Goal:** Expand image to fill entire available width

### 2. Remove Arrow Indicators ❌
**Problem:** Arrow indicators appearing during scroll are not needed
**Current:** 5 indicators show at 3s, 10s, 22s, 35s, 45s
**Goal:** Remove all visual indicators completely

### 3. White Space at End ❌
**Problem:** Large white space when scroll completes
**Current:** Small restart button at bottom
**Goal:** Elegant modal popup (matching start screen design)

---

## 🔧 Technical Changes Required

### Change 1: Remove Gray Space (Expand Image to Full Width)

**File:** `src/mpp-portal-scroll.html`
**Section:** CSS - `.scroll-viewport` and `.scroll-container`

**Current Code:**
```css
.scroll-viewport {
    width: 100%;
    max-width: 800px;  /* ← LIMITING WIDTH */
    height: 600px;
    margin: 0 auto;
    overflow: hidden;
    position: relative;
    background: #f5f5f5;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.scroll-container img {
    width: 800px;  /* ← FIXED WIDTH */
    height: auto;
    display: block;
}
```

**New Code:**
```css
.scroll-viewport {
    width: 100%;
    max-width: 100%;  /* ← FILL AVAILABLE WIDTH */
    height: 600px;
    margin: 0 auto;
    overflow: hidden;
    position: relative;
    background: #1e3a5f;  /* Match DoD blue instead of gray */
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.scroll-container img {
    width: 100%;  /* ← RESPONSIVE WIDTH */
    height: auto;
    display: block;
}
```

**Result:** Image will scale to fill entire viewport width

---

### Change 2: Remove All Arrow Indicators

**File:** `src/mpp-portal-scroll.html`
**Section:** HTML and JavaScript

**Option A: Hide with CSS (Simplest)**
```css
.indicator {
    display: none !important;  /* ← HIDE ALL INDICATORS */
}
```

**Option B: Remove HTML Elements (Cleanest)**
Delete these 5 divs from HTML:
```html
<!-- DELETE THESE -->
<div id="indicator1" class="indicator" role="status" aria-live="polite">
    <span>JOIN NOW button</span>
</div>
<div id="indicator2" class="indicator" role="status" aria-live="polite">
    <span>Subcontracting pool</span>
</div>
<div id="indicator3" class="indicator" role="status" aria-live="polite">
    <span>Technical education</span>
</div>
<div id="indicator4" class="indicator" role="status" aria-live="polite">
    <span>MPP Summit logo</span>
</div>
<div id="indicator5" class="indicator" role="status" aria-live="polite">
    <span>Contact form</span>
</div>
```

**Option C: Remove JavaScript Logic**
Delete or comment out indicator code in `showIndicator()` method and `animate()` method.

**Recommendation:** Use **Option A** (CSS hide) - fastest, easily reversible if needed later.

---

### Change 3: Elegant Restart Modal (Match Start Screen)

**File:** `src/mpp-portal-scroll.html`
**Section:** HTML and CSS

**Add New HTML After Play Modal:**
```html
<!-- Restart Modal (appears at end) -->
<div id="restartModal" class="modal-overlay" style="display: none;">
    <div class="modal-content">
        <h1>Tour Complete!</h1>
        <p>Experience the Mentor-Protégé Program Portal again</p>
        <button id="restartModalBtn" class="modal-button" aria-label="Restart the MPP Portal tour">
            ▶ Restart Tour
        </button>
    </div>
</div>
```

**Add CSS (reuse existing modal styles):**
```css
/* Restart modal uses same styles as play modal */
#restartModal {
    /* Inherits from .modal-overlay */
}

#restartModal .modal-content {
    /* Same styling as start modal */
}

#restartModalBtn {
    /* Same styling as play button */
}
```

**Update JavaScript `onComplete()` Method:**
```javascript
onComplete() {
    this.isRunning = false;
    this.currentTime = 0;
    this.scrollContainer.style.transform = 'translateY(0)';

    // Remove small restart button (old approach)
    // const restartBtn = document.getElementById('restartBtn');
    // if (restartBtn) restartBtn.style.display = 'block';

    // Show elegant restart modal (NEW)
    const restartModal = document.getElementById('restartModal');
    restartModal.style.display = 'flex';
    restartModal.style.opacity = '0';

    // Fade in animation
    requestAnimationFrame(() => {
        restartModal.style.transition = 'opacity 0.5s ease-in-out';
        restartModal.style.opacity = '1';
    });

    // Announce to screen readers
    this.announcer.textContent = 'Tour complete. Click Restart Tour to experience again.';
}
```

**Update JavaScript `restart()` Method:**
```javascript
restart() {
    // Hide restart modal
    const restartModal = document.getElementById('restartModal');
    restartModal.style.display = 'none';

    // Reset everything
    this.currentTime = 0;
    this.isRunning = false;
    this.scrollContainer.style.transform = 'translateY(0)';
    this.viewport.style.display = 'none';

    // Show play modal again
    this.playModal.style.display = 'flex';

    // Reset audio
    if (this.audio) {
        this.audio.pause();
        this.audio.currentTime = 0;
    }

    // Focus play button
    this.playBtn.focus();

    // Announce
    this.announcer.textContent = 'Tour restarted. Click Start Tour to begin again.';
}
```

**Wire Up Restart Modal Button:**
```javascript
// In constructor, add event listener
const restartModalBtn = document.getElementById('restartModalBtn');
restartModalBtn.addEventListener('click', () => this.restart());

// Keyboard support
restartModalBtn.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.restart();
    }
});
```

---

## 📦 Implementation Steps

### Step 1: Modify HTML Template ✅
1. Open `src/mpp-portal-scroll.html`
2. Add CSS to hide indicators: `.indicator { display: none !important; }`
3. Change viewport width: `max-width: 100%;`
4. Change image width: `width: 100%;`
5. Add restart modal HTML
6. Add restart modal CSS
7. Update JavaScript `onComplete()` method
8. Update JavaScript `restart()` method
9. Add event listeners for restart modal button

### Step 2: Re-embed Assets ✅
```bash
cd C:\Users\MarieLexisDad\MPP-Portal-Course\assets
python embed_assets.py
```

### Step 3: Create New Zip File ✅
```bash
cd C:\Users\MarieLexisDad\MPP-Portal-Course
# Delete old zip
rm MPP-Portal-Scroll-for-Rise.zip
# Create new zip with updated index.html
powershell -Command "Compress-Archive -Path index.html -DestinationPath MPP-Portal-Scroll-for-Rise.zip -Force"
```

### Step 4: Test Locally ✅
```bash
start index.html
# Verify:
# - Image fills width (no gray space)
# - No arrow indicators appear
# - Restart modal appears at end with same design as start
```

### Step 5: Commit and Push ✅
```bash
git add -A
git commit -m "Improvements: Full-width image, removed indicators, elegant restart modal"
git push origin main
```

### Step 6: Deploy to Rise ✅
1. Upload new `MPP-Portal-Scroll-for-Rise.zip`
2. Test in Rise preview
3. Verify all improvements
4. Publish!

---

## 🎯 Expected Results

### Before vs After

| Feature | Before | After |
|---------|--------|-------|
| **Image Width** | 800px max (gray space) | 100% width (no gray space) |
| **Arrow Indicators** | 5 arrows at timed intervals | None (hidden) |
| **Restart UX** | Small button at bottom | Elegant modal popup |
| **Restart Design** | Simple button | Same elegant design as start |
| **White Space** | Large white space at end | Covered by modal overlay |

### Visual Improvements

1. **Full-Width Image** ✨
   - Image fills entire available width
   - No gray sidebars
   - More immersive experience
   - Better use of screen real estate

2. **Cleaner Animation** ✨
   - No distracting arrows
   - Focus on content
   - Smoother visual experience
   - Audio narration guides attention

3. **Elegant Completion** ✨
   - Modal overlay covers white space
   - Consistent design language
   - Professional appearance
   - Same DoD blue gradient
   - Same button styling

---

## 🧪 Testing Checklist

After implementing changes:

- [ ] Image fills viewport width (no gray space)
- [ ] Image scales responsively
- [ ] No arrow indicators appear during scroll
- [ ] Scroll animation still smooth (50 seconds)
- [ ] Audio still plays correctly
- [ ] Restart modal appears at completion
- [ ] Restart modal has DoD blue gradient background
- [ ] Restart modal button matches start button style
- [ ] Restart modal covers white space
- [ ] Restart button works correctly
- [ ] Returns to start modal on restart
- [ ] Keyboard navigation still works (Enter, Space, Escape)
- [ ] Mobile responsive (test on phone)
- [ ] Tablet responsive
- [ ] Desktop responsive

---

## 📝 Files to Modify

1. **src/mpp-portal-scroll.html** - Main template file
   - CSS changes (viewport, image, indicators)
   - HTML additions (restart modal)
   - JavaScript changes (onComplete, restart methods)

2. **assets/embed_assets.py** - Re-run to create new complete file

3. **index.html** - Auto-generated from step 2

4. **MPP-Portal-Scroll-for-Rise.zip** - Recreate with new index.html

---

## ⏱️ Estimated Time

- **Code Changes:** 15 minutes
- **Testing:** 10 minutes
- **Re-embedding & Zip Creation:** 5 minutes
- **Total:** ~30 minutes

---

## 🚀 Ready to Implement?

Once you approve this plan, I will:
1. Make all code changes
2. Re-embed assets
3. Create new zip file
4. Test locally
5. Commit and push to GitHub
6. Provide you with the updated zip for Rise deployment

**Approval needed to proceed with implementation.**

---

**Created:** November 27, 2025
**Status:** ⏳ Awaiting Approval
**Next Step:** Implement changes to `src/mpp-portal-scroll.html`
