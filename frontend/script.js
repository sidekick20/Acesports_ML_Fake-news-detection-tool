// ── Example texts for quick test buttons ──────────────────────────────────────
const examples = {
  clickbait:     "You won't BELIEVE what this politician did behind closed doors — doctors are shocked!",
  real:          "The Federal Reserve raised interest rates by 25 basis points on Wednesday, citing persistent inflation concerns.",
  ragebait:      "THEY ARE COMING FOR YOUR CHILDREN: Government secretly plans to ban homeschooling nationwide!!!",
  pseudoscience: "Scientists confirm drinking lemon water every morning CURES cancer and reverses aging completely."
};

function fillExample(type) {
  const textarea = document.getElementById('news-input');
  textarea.value = examples[type] || '';
  updateCharCount();
  // Clear any previous result when loading an example
  const resultBox = document.getElementById('result');
  resultBox.style.display = 'none';
  resultBox.className = 'result-box';
}

// ── Character counter ─────────────────────────────────────────────────────────
function updateCharCount() {
  const textarea = document.getElementById('news-input');
  const counter  = document.getElementById('char-count');
  const len = textarea.value.length;
  counter.textContent = `${len}/2000`;
  counter.style.color = len > 1800 ? '#ef4444' : '#94a3b8';
}

document.getElementById('news-input').addEventListener('input', updateCharCount);

// ── Clear button ──────────────────────────────────────────────────────────────
document.getElementById('clear-btn').addEventListener('click', () => {
  const textarea = document.getElementById('news-input');
  textarea.value = '';
  updateCharCount();

  const resultBox = document.getElementById('result');
  resultBox.style.display = 'none';
  resultBox.className = 'result-box';

  document.getElementById('spinner').style.display = 'none';
});

// ── Main analysis ─────────────────────────────────────────────────────────────
document.getElementById('analyze-btn').addEventListener('click', async () => {
  const textarea  = document.getElementById('news-input');
  const resultBox = document.getElementById('result');
  const spinner   = document.getElementById('spinner');
  const btn       = document.getElementById('analyze-btn');

  const text = textarea.value.trim();
  if (!text) {
    textarea.style.borderColor = '#ef4444';
    textarea.style.boxShadow   = '0 0 0 3px rgba(239,68,68,0.15)';
    setTimeout(() => {
      textarea.style.borderColor = '#cbd5e1';
      textarea.style.boxShadow   = 'none';
    }, 1500);
    return;
  }

  // Loading state
  btn.disabled    = true;
  btn.innerHTML   = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
  spinner.style.display  = 'block';
  resultBox.style.display = 'none';
  resultBox.className     = 'result-box';

  try {
    const response = await fetch('/predict', {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ text })
    });

    if (!response.ok) throw new Error(`Server error (${response.status})`);

    const data = await response.json();
    const isFake = data.label === 'FAKE';

    const keywordsHTML = data.keywords && data.keywords.length
      ? `<div class="keywords-row">
           <span class="keywords-label"><i class="fas fa-key"></i> Key signals:</span>
           <div class="keyword-tags">
             ${data.keywords.map(k => `<span class="keyword-tag">${k}</span>`).join('')}
           </div>
         </div>`
      : '';

    const confidenceBar = `
      <div class="confidence-bar-wrap">
        <div class="confidence-bar-track">
          <div class="confidence-bar-fill ${isFake ? 'fake' : 'real'}"
               style="width: ${data.confidence}%"></div>
        </div>
        <span class="confidence-label">${data.confidence}% confidence</span>
      </div>`;

    resultBox.className = `result-box ${isFake ? 'result-fake' : 'result-real'}`;
    resultBox.innerHTML = `
      <div class="result-header">
        <div class="result-icon">${isFake ? '🚨' : '✅'}</div>
        <div>
          <div class="result-verdict">${isFake ? 'Likely Fake News' : 'Likely Real News'}</div>
          <div class="result-sub">${isFake
            ? 'This article shows patterns common in misinformation.'
            : 'This article appears consistent with credible reporting.'}</div>
        </div>
      </div>
      ${confidenceBar}
      ${keywordsHTML}
    `;
    resultBox.style.display = 'block';

    // Smooth scroll to result
    resultBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

  } catch (err) {
    resultBox.className = 'result-box result-error';
    resultBox.innerHTML = `
      <div class="result-header">
        <div class="result-icon">⚠️</div>
        <div>
          <div class="result-verdict">Connection Error</div>
          <div class="result-sub">${err.message} — make sure Flask is running on port 5000.</div>
        </div>
      </div>`;
    resultBox.style.display = 'block';
  } finally {
    spinner.style.display = 'none';
    btn.disabled  = false;
    btn.innerHTML = '<i class="fas fa-microchip"></i> Run AI Analysis';
  }
});