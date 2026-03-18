# Demo NLP Model
# This script demonstrates a simple text classification pipeline

import re
from collections import Counter

def preprocess(text):
    """Lowercase and remove punctuation."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def bag_of_words(corpus):
    """Create a basic bag-of-words representation."""
    word_counts = Counter()
    for sentence in corpus:
        tokens = preprocess(sentence).split()
        word_counts.update(tokens)
    return word_counts

if __name__ == "__main__":
    sample_data = [
        "Natural language processing is fascinating",
        "Machine learning helps solve NLP tasks",
        "Deep learning models outperform classical methods"
    ]

    bow = bag_of_words(sample_data)
    print("Top 5 words:", bow.most_common(5))
```

4. Scroll down to **"Commit changes"**
   - Add a commit message like: `Add demo NLP script`
   - Leave **"Commit directly to the main branch"** selected
   - Click **"Commit changes"**

Your file is now live on GitHub! 🎉

---

## Step 4 — Anonymize It on Anonymous GitHub

Now let's do the actual test run:

1. Go to **[https://anonymous.4open.science](https://anonymous.4open.science)**
2. Click **"Sign in with GitHub"** and authorize
3. Click **"New anonymization"**
4. Fill in:

| Field | Value |
|---|---|
| **Repository** | Select `demo-acl-srw` from dropdown |
| **Title** | `NLP-Demo-Submission` |
| **Description** | `Code for ACL SRW anonymous review` |

5. Click **"Anonymize"**
6. Wait ~10–30 seconds, then copy the generated link (starts with `https://anonymous.4open.science/r/...`)

---

## Step 5 — Verify It's Truly Anonymous

1. **Copy** the anonymous link
2. Open a **new incognito window** (Ctrl+Shift+N on Chrome/Edge)
3. Paste and open the link
4. Check:
   - ✅ No GitHub username visible
   - ✅ No profile picture or bio
   - ✅ Code is visible and readable
   - ✅ Files look clean — no identifying info in comments

If all boxes check out, this is exactly the link you'd paste into your ACL SRW paper submission.

---

## Quick Visual Summary
```
github.com → Sign Up → New Repo (Public) → Add File → Commit
     ↓
anonymous.4open.science → Sign in → Anonymize Repo → Get Link
     ↓
Paste link in your ACL SRW paper ✅
