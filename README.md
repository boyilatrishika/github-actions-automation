# Search Engine Indexing Automation

Automatically submit your website URLs to Google Search Console and Bing Webmaster Tools using GitHub Actions.

## Features

✨ **Automated Scheduling**
- Daily automatic execution at 03:00 UTC (8:30 AM IST)
- Manual trigger via GitHub Actions "Run workflow" button
- Configurable execution time via cron expression

🔍 **Multi-Search Engine Support**
- **Google Search Console** - Submit URLs via Indexing API
- **Bing Webmaster Tools** - Submit URLs via URL Submission API

📝 **URL Management**
- Simple text file format (`urls.txt`)
- One URL per line
- Support for comments (lines starting with `#`)
- No special formatting required

🛡️ **Security**
- Environment variable-based secret management
- GCP service account key authentication
- Sensitive data excluded via `.gitignore`

📊 **Monitoring & Reporting**
- Detailed execution logs for each submission
- Success/failure tracking per URL
- GitHub Actions workflow summary
- Optional debug mode for troubleshooting

🚨 **Error Handling**
- Individual URL failure isolation
- Graceful error handling and logging
- Detailed error messages for debugging

## Quick Start

### 1. Add URLs to Index

Edit `urls.txt` and add your website URLs:

```txt
https://example.com
https://example.com/about
https://example.com/blog
https://example.com/contact
```

Comments are supported:
```txt
# Homepage
https://example.com

# Important pages
https://example.com/about
https://example.com/contact
```

### 2. Configure GitHub Secrets

In your repository settings, add the following secrets:

**Settings → Secrets and variables → Actions → New repository secret**

| Secret Name | Value |
|------------|-------|
| `DOMAIN_URL` | Your domain (e.g., `https://example.com`) |
| `GCP_SA_KEY` | Google Cloud service account JSON key |
| `BING_API_KEY` | Bing Webmaster Tools API key |

### 3. Enable Google Search Console API

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create or select a project
3. Enable the "Indexing API"
4. Create a service account
5. Generate and download the JSON key
6. Add the domain to your Google Search Console property
7. Grant the service account access to your property

### 4. Get Bing Webmaster Tools API Key

1. Visit [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Sign in and add your site
3. Go to API Access
4. Generate and copy your API key

### 5. Run the Workflow

**Automatic:** The workflow runs daily at 03:00 UTC

**Manual:** 
1. Go to **Actions** tab in your repository
2. Select "Search Engine Indexing Automation"
3. Click "Run workflow"
4. Optionally enable debug mode for detailed logging
5. Click "Run workflow"

## Workflow Files

```
.
├── .github/
│   └── workflows/
│       └── search-indexing.yml    # Main workflow file
├── urls.txt                        # URLs to submit
├── README.md                       # This file
├── DEPLOYMENT.md                   # Setup & troubleshooting
└── .gitignore                      # Ignore sensitive files
```

## Environment Variables

**Required Secrets:**

- `DOMAIN_URL`: Your domain URL (used for Bing API)
- `GCP_SA_KEY`: Google Cloud service account key (JSON)
- `BING_API_KEY`: Bing Webmaster Tools API key

## Workflow Inputs

When running manually, you can configure:

- **debug_mode**: Enable detailed logging (true/false, default: false)

## Monitoring

Check workflow execution status:

1. **Actions Tab**: View all workflow runs
2. **Step Summary**: See detailed execution report
3. **Logs**: Click on any step for detailed logs
4. **Search Console**: Verify URL submissions in [Google Search Console](https://search.google.com/search-console)
5. **Bing Webmaster**: Verify URL submissions in [Bing Webmaster Tools](https://www.bing.com/webmasters)

## Schedule

**Default:** Daily at 03:00 UTC (8:30 AM IST)

To change the schedule, edit `.github/workflows/search-indexing.yml`:

```yaml
on:
  schedule:
    - cron: '0 3 * * *'  # Change the cron expression here
```

Common cron expressions:
- `0 0 * * *` - Daily at midnight UTC
- `0 12 * * *` - Daily at noon UTC
- `0 3 * * 0` - Weekly on Sunday at 03:00 UTC
- `0 3 1 * *` - Monthly on the 1st at 03:00 UTC

## Troubleshooting

For detailed troubleshooting steps, see [DEPLOYMENT.md](DEPLOYMENT.md)

## Best Practices

✅ **Do:**
- Keep `urls.txt` updated with current URLs
- Run workflow after publishing new pages
- Monitor workflow execution logs
- Test with a small URL set first
- Keep secrets secure and never commit them

❌ **Don't:**
- Commit GCP keys or API keys to the repository
- Submit the same URL multiple times unnecessarily
- Store secrets in plain text files
- Share your API keys

## API Rate Limits

**Google Search Console Indexing API:**
- Rate limit: 200 requests per 15 seconds
- Daily quota: Generous (depends on your tier)

**Bing Webmaster Tools:**
- Rate limit: Varies by account level
- Batch size: Up to 1,000 URLs per request

## Support & Documentation

- [Google Search Console API Docs](https://developers.google.com/search/docs/indexing-api)
- [Bing Webmaster Tools API Docs](https://www.bing.com/webmasters/help/api-overview-1e1b57e4)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## License

MIT License - Feel free to use this for your projects!

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

**Need help?** Check [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive setup and troubleshooting guide.
