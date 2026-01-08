# Deployment & Setup Guide

Complete step-by-step setup and troubleshooting guide for the Search Engine Indexing Automation workflow.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Google Cloud Setup](#google-cloud-setup)
3. [Bing Webmaster Setup](#bing-webmaster-setup)
4. [GitHub Repository Setup](#github-repository-setup)
5. [Workflow Configuration](#workflow-configuration)
6. [Testing](#testing)
7. [Troubleshooting](#troubleshooting)
8. [FAQs](#faqs)

---

## Prerequisites

- GitHub account with repository access
- Google Cloud account
- Bing Webmaster Tools account
- At least one domain for indexing

---

## Google Cloud Setup

### Step 1: Create a Google Cloud Project

1. Visit [Google Cloud Console](https://console.cloud.google.com)
2. Click the project selector at the top
3. Click "New Project"
4. Enter project name: `Search-Indexing-Automation`
5. Click "Create"
6. Wait for the project to be created (may take a minute)

### Step 2: Enable the Indexing API

1. In the Cloud Console, go to **APIs & Services > Library**
2. Search for "Indexing API"
3. Click on "Indexing API"
4. Click "Enable"
5. You'll see "API enabled" confirmation

### Step 3: Create a Service Account

1. Go to **APIs & Services > Credentials**
2. Click "Create Credentials" at the top
3. Select "Service Account"
4. Fill in the form:
   - **Service account name:** `search-indexing-bot`
   - **Description:** `Automated search engine indexing`
5. Click "Create and Continue"
6. Skip the optional steps and click "Done"

### Step 4: Generate Service Account Key

1. Go to **APIs & Services > Credentials**
2. Under "Service Accounts", click on the service account you just created
3. Go to the **Keys** tab
4. Click "Add Key" > "Create new key"
5. Select **JSON** format
6. Click "Create"
7. A JSON file will download automatically
8. **IMPORTANT:** Save this file securely. You'll need its contents for GitHub secrets.

### Step 5: Configure Google Search Console

1. Visit [Google Search Console](https://search.google.com/search-console)
2. Add your domain property if not already added
3. Go to **Settings > Users and permissions**
4. Click "Add user"
5. Paste the service account email (found in the downloaded JSON as `client_email`)
6. Select role: **Owner**
7. Click "Invite"
8. Accept the invitation (you'll receive an email)

---

## Bing Webmaster Setup

### Step 1: Add Your Site to Bing Webmaster Tools

1. Visit [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Sign in with your Microsoft account
3. Click "Add a site"
4. Enter your domain URL
5. Verify ownership (follow Bing's verification process)
6. Click "Next"

### Step 2: Generate API Key

1. In Bing Webmaster Tools, go to **Settings > API Access**
2. Click "Generate API key"
3. Copy the generated API key
4. **IMPORTANT:** Store this securely. You'll need it for GitHub secrets.

---

## GitHub Repository Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/github-actions-automation.git
cd github-actions-automation
```

### Step 2: Add Repository Secrets

1. Go to your repository on GitHub
2. Navigate to **Settings > Secrets and variables > Actions**
3. Click "New repository secret"

#### Secret 1: DOMAIN_URL

- **Name:** `DOMAIN_URL`
- **Value:** Your domain URL (e.g., `https://example.com`)
- Click "Add secret"

#### Secret 2: GCP_SA_KEY

- **Name:** `GCP_SA_KEY`
- **Value:** Contents of the JSON key file you downloaded from Google Cloud
  - Open the downloaded JSON file with a text editor
  - Copy the entire contents
  - Paste it as the secret value
- Click "Add secret"

#### Secret 3: BING_API_KEY

- **Name:** `BING_API_KEY`
- **Value:** The API key from Bing Webmaster Tools
- Click "Add secret"

### Step 3: Update URLs File

1. Edit `urls.txt` in the repository
2. Replace example URLs with your actual website URLs
3. One URL per line
4. Commit and push the changes:

```bash
git add urls.txt
git commit -m "Update URLs for indexing"
git push origin main
```

---

## Workflow Configuration

### Default Configuration

The workflow is configured to:
- Run daily at **03:00 UTC (8:30 AM IST)**
- Be manually triggerable via GitHub Actions
- Use 30-minute timeout
- Continue on errors to attempt all URLs

### Changing the Schedule

To change the execution time:

1. Edit `.github/workflows/search-indexing.yml`
2. Find the `schedule` section:

```yaml
on:
  schedule:
    - cron: '0 3 * * *'  # 03:00 UTC daily
```

3. Modify the cron expression:
   - Format: `minute hour day-of-month month day-of-week`
   - Examples:
     - `'0 0 * * *'` - Daily at midnight UTC
     - `'0 3 * * 0'` - Weekly on Sunday at 03:00 UTC
     - `'0 3 1 * *'` - Monthly on the 1st at 03:00 UTC
     - `'0 */6 * * *'` - Every 6 hours

4. Commit and push the changes

---

## Testing

### Test 1: Manual Workflow Execution

1. Go to your repository
2. Click **Actions** tab
3. Select "Search Engine Indexing Automation" workflow
4. Click "Run workflow" button
5. Select "main" branch
6. Optionally enable "debug mode"
7. Click "Run workflow"
8. Monitor the execution in real-time

### Test 2: Verify Submissions

**Google Search Console:**
1. Visit [Google Search Console](https://search.google.com/search-console)
2. Go to your property
3. Navigate to **Indexing > Indexed pages**
4. Your URLs should appear here within 24-48 hours

**Bing Webmaster Tools:**
1. Visit [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Go to your site
3. Navigate to **URL Submissions > Submitted URLs**
4. Your URLs should appear in the submission history

### Test 3: Check Logs

1. In the workflow run, click on any failed/successful step
2. Expand the logs to see detailed output
3. Look for checkmarks (✓) for successful submissions
4. Look for error messages (✗) for failures

---

## Troubleshooting

### Issue: "GCP key validation failed"

**Cause:** Invalid JSON format in GCP_SA_KEY secret

**Solution:**
1. Download the GCP service account key again
2. Verify it's valid JSON (use [jsonlint.com](https://jsonlint.com))
3. Update the GitHub secret with correct JSON
4. Re-run the workflow

### Issue: "BING_API_KEY not configured"

**Cause:** BING_API_KEY secret is missing

**Solution:**
1. Go to GitHub Settings > Secrets
2. Verify BING_API_KEY secret exists
3. If missing, add it from Bing Webmaster Tools
4. Re-run the workflow

### Issue: "Google submission error: 403 Forbidden"

**Cause:** Service account doesn't have permission to your Search Console property

**Solution:**
1. Verify service account email in Google Cloud
2. Go to Google Search Console Settings > Users and permissions
3. Add the service account with Owner role
4. Wait 5-10 minutes for changes to propagate
5. Re-run the workflow

### Issue: "No URLs found to submit"

**Cause:** `urls.txt` file is missing or empty

**Solution:**
1. Ensure `urls.txt` exists in repository root
2. Add URLs (one per line)
3. Commit and push changes
4. Re-run the workflow

### Issue: "Workflow fails silently"

**Solution:**
1. Run workflow manually with debug mode enabled
2. Check the detailed logs in the workflow run
3. Look for Python stack traces or error messages
4. Verify all secrets are correctly configured

### Issue: "URLs not appearing in Search Console after 48 hours"

**Cause:** Various factors - newly added site, robots.txt blocking, etc.

**Solution:**
1. Verify URLs are valid and accessible
2. Check if robots.txt allows indexing
3. Verify metadata (title, description) are present
4. Wait longer (can take weeks for some URLs)
5. Check Search Console for any crawl errors

---

## FAQs

### Q: How often should I run the workflow?

A: Daily is recommended for fresh content. You can adjust the schedule in the YAML file based on your content update frequency.

### Q: Can I submit URLs from multiple domains?

A: Currently, the workflow uses a single DOMAIN_URL for Bing. For multiple domains, you can:
1. Create separate workflows for each domain
2. Or use environment-specific variables

### Q: What's the rate limit for submissions?

A: Google Indexing API allows 200 requests per 15 seconds. The workflow respects these limits.

### Q: Can I run the workflow on a specific branch?

A: Yes, edit the workflow file's `on` section to specify branches:

```yaml
on:
  push:
    branches:
      - main
  schedule:
    - cron: '0 3 * * *'
```

### Q: How long does the workflow take to complete?

A: Typically 5-15 minutes depending on number of URLs and API response times.

### Q: Can I use this for a subdomain?

A: Yes, just update DOMAIN_URL to your subdomain (e.g., `https://blog.example.com`).

### Q: What if I want to skip certain URLs?

A: Add lines starting with `#` to `urls.txt`:

```txt
https://example.com
# https://example.com/private  <- Will be skipped
https://example.com/public
```

### Q: Can I submit sitemaps instead of individual URLs?

A: The current workflow supports individual URLs. For sitemap submission:
- Google Search Console: Submit via UI
- Bing Webmaster: Submit via UI or API

### Q: Is my API key secure?

A: Yes, GitHub Secrets are encrypted and never exposed in logs or history.

---

## Support

For additional help:
- Check the main [README.md](README.md)
- Review workflow logs in GitHub Actions
- Visit [Google Search Console Help](https://support.google.com/webmasters)
- Visit [Bing Webmaster Tools Help](https://www.bing.com/webmasters/help)

