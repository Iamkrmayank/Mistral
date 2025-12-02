# How to Set Up Secrets for Streamlit App

## Step-by-Step Guide

### Step 1: Create the Secrets File

1. Go to your project root directory: `C:\mistral-ocr-api`
2. Create a folder named `.streamlit` (if it doesn't exist)
3. Inside `.streamlit`, create a file named `secrets.toml`

**Full path should be:** `C:\mistral-ocr-api\.streamlit\secrets.toml`

### Step 2: Get Your API Credentials

You need 3 values from your `.env` file or Azure portal:

1. **MISTRAL_OCR_ENDPOINT** - Your Mistral OCR API endpoint URL
2. **API_KEY** - Your Mistral API key
3. **MISTRAL_MODEL** - Model name (usually `mistral-document-ai-2505`)

### Step 3: Fill in the Secrets File

Open `.streamlit/secrets.toml` and add:

```toml
[mistral]
ocr_endpoint = "https://your-actual-endpoint.services.ai.azure.com/providers/mistral/azure/ocr"
api_key = "your_actual_api_key_here"
model = "mistral-document-ai-2505"
```

**Example format (replace with your actual values):**
```toml
[mistral]
ocr_endpoint = "https://your-endpoint-12345.services.ai.azure.com/providers/mistral/azure/ocr"
api_key = "your_actual_api_key_here_replace_with_real_key"
model = "mistral-document-ai-2505"
```

### Step 4: Verify the File Structure

Your project should look like this:
```
mistral-ocr-api/
├── .streamlit/
│   ├── secrets.toml          ← Your actual secrets (NOT in git)
│   └── secrets.toml.example  ← Example file (safe to commit)
├── app/
│   ├── streamlit_app.py
│   └── mistral_ocr-v6.py
└── ...
```

### Step 5: Run the App

```bash
streamlit run app/streamlit_app.py
```

The app will:
- ✅ Check if secrets are configured
- ✅ Show an error if secrets are missing
- ✅ Use secrets automatically when running OCR

## Important Notes

1. **Never commit `secrets.toml` to git!**
   - It's already in `.gitignore`
   - Only commit `secrets.toml.example`

2. **Where to get values:**
   - Check your existing `.env` file
   - Or get them from Azure portal / Mistral dashboard

3. **File location:**
   - Must be in `.streamlit/secrets.toml` (project root)
   - NOT in `app/.streamlit/secrets.toml`

4. **Format:**
   - Use TOML format (not JSON)
   - Use double quotes for strings
   - Section name is `[mistral]`

## Troubleshooting

### Error: "Secrets not configured"
- Check if `.streamlit/secrets.toml` exists
- Check if file is in correct location (project root, not app folder)
- Check if all 3 keys are present: `ocr_endpoint`, `api_key`, `model`

### Error: "Could not load secrets"
- Check TOML syntax (use double quotes, proper brackets)
- Make sure no extra spaces or special characters

### Still not working?
- Restart Streamlit app after creating/editing secrets.toml
- Check file permissions
- Verify values are correct (no typos)

