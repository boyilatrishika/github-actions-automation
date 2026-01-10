# Bluesky Posting Automation

This workflow automates posting content to Bluesky Social using GitHub Actions.

## Prerequisites

Before setting up this automation, you need:

1. **Bluesky Account**: An active account at [bsky.app](https://bsky.app)
2. **GitHub Repository**: Access to this repository with settings permissions

## Setup Instructions

### Step 1: Generate Bluesky App Password

1. Go to [bsky.app/settings/app-passwords](https://bsky.app/settings/app-passwords)
2. Click "+ Add App Password"
3. Give it a name (e.g., "github-actions")
4. Copy the generated password (you'll only see it once)

### Step 2: Add GitHub Secrets

1. Go to your GitHub repository → **Settings** → **Secrets and variables** → **Actions**
2. Click "New repository secret" and add:
   - **Name**: `BSKY_IDENTIFIER`
   - **Value**: Your Bluesky handle (e.g., `username.bsky.social`)
3. Click "New repository secret" again and add:
   - **Name**: `BSKY_PASSWORD`
   - **Value**: The app password you generated in Step 1

## Using the Workflow

### Automatic Posting (Daily)

The workflow is configured to post automatically every day at **9:00 AM UTC**. You can modify the schedule by editing the `cron` value in `.github/workflows/bluesky-post.yml`:

```yaml
on:
  schedule:
    - cron: '0 9 * * *'  # Change this to your preferred time
```

### Manual Posting

1. Go to your repository → **Actions** tab
2. Select "Post to Bluesky" workflow
3. Click "Run workflow"
4. Enter your post content
5. Click "Run workflow"

## Workflow Configuration

### File Location
- `.github/workflows/bluesky-post.yml`

### Default Post Content
```
Daily automated post from GitHub Actions! Check out my automation workflows.
```

### Trigger Events
- **Schedule**: Every day at 9:00 AM UTC
- **Manual**: Via `workflow_dispatch`

## Monitoring

1. Go to **Actions** tab in your repository
2. Select the "Post to Bluesky" workflow
3. View workflow run logs to confirm posts were successful
4. Check your Bluesky feed to verify posts appear

## Advanced Configuration

### Changing the Schedule

Edit `.github/workflows/bluesky-post.yml` and modify the cron expression:
- `0 9 * * *` - Every day at 9:00 AM UTC
- `0 9 * * 1` - Every Monday at 9:00 AM UTC
- `0 9,18 * * *` - Every day at 9 AM and 6 PM UTC

Use [crontab.guru](https://crontab.guru) to generate custom schedules.

### Custom Post Content

You can customize the post content in the workflow file or use the manual trigger to specify custom messages.

## Troubleshooting

### Workflow fails to run
- Verify `BSKY_IDENTIFIER` and `BSKY_PASSWORD` secrets are correctly set
- Check that the app password hasn't been revoked from Bluesky settings

### Posts not appearing
- Check workflow logs in the Actions tab
- Verify your Bluesky account is not rate-limited
- Ensure the post content doesn't violate Bluesky's community guidelines

### Authentication errors
- Regenerate app password in Bluesky settings
- Update the `BSKY_PASSWORD` secret in GitHub with the new password

## Security Notes

- The app password is encrypted in GitHub Secrets and never exposed
- App passwords have limited permissions compared to your main account password
- You can revoke app passwords anytime from Bluesky settings without affecting your main account
- Never commit your app password to version control

## References

- [Bluesky App Password Documentation](https://bsky.app/settings/app-passwords)
- [GitHub Actions Secrets](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)
- [zentered/bluesky-post-action](https://github.com/marketplace/actions/bluesky-post-action)

## Support

For issues with the workflow, check:
1. The Actions logs in your GitHub repository
2. Your Bluesky account settings
3. GitHub Actions documentation
