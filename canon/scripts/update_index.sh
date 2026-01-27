#!/bin/bash
# MIRRORNODE Index Update Automation
# Runs the indexer and commits changes if repos have been added/updated

set -euo pipefail

# ================================================================
# PREFLIGHT CHECKS
# ================================================================

echo "🔍 Running preflight checks..."

# Verify GitHub token
if [ -z "${GITHUB_TOKEN:-}" ]; then
  echo "❌ Error: GITHUB_TOKEN environment variable not set"
  echo "   Set it with: export GITHUB_TOKEN='your_token_here'"
  exit 1
fi

# Verify we're in the right directory
if [ ! -d "canon/scripts" ]; then
  echo "❌ Error: Not in mirrornode-index repository root"
  echo "   Current directory: $(pwd)"
  exit 1
fi

# Verify Python is available
if ! command -v python3 &> /dev/null; then
  echo "❌ Error: python3 not found"
  exit 1
fi

echo "✅ Preflight checks passed"
echo ""

# ================================================================
# SYNC WITH REMOTE
# ================================================================

echo "📥 Syncing with remote..."

# Stash any local changes temporarily
STASHED=false
if ! git diff-index --quiet HEAD --; then
  git stash push -q -u -m "Auto-stash before index update"
  STASHED=true
fi

git pull --rebase --quiet || {
  echo "❌ Error: Failed to pull latest changes"
  if [ "$STASHED" = true ]; then
    git stash pop -q
  fi
  exit 1
}

# Restore stashed changes if any
if [ "$STASHED" = true ]; then
  git stash pop -q 2>/dev/null || true
fi

echo "✅ Synced with remote"
echo ""

# ================================================================
# RUN INDEXER
# ================================================================

echo "🔄 Running MIRRORNODE indexer..."
if python3 canon/scripts/build_index.py; then
  echo "✅ Indexer completed successfully"
else
  echo "❌ Error: Indexer failed"
  exit 1
fi
echo ""

# ================================================================
# COMMIT & PUSH CHANGES
# ================================================================

echo "📦 Staging generated files..."
git add repos.json index_metadata.json summaries/ components/ 2>/dev/null || true

if git diff --cached --quiet; then
  echo "✨ No changes detected - index is up to date"
  echo "✅ MIRRORNODE INDEX UPDATE COMPLETE (no changes)"
  exit 0
fi

# Show what changed
echo "📊 Changes detected:"
git diff --cached --stat
echo ""

echo "📝 Committing index update..."
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
git commit -m "🔄 Automated index update - ${TIMESTAMP}" --quiet

echo "📤 Pushing to remote..."
git push --quiet || {
  echo "❌ Error: Failed to push changes"
  exit 1
}

echo "✅ MIRRORNODE INDEX UPDATE COMPLETE"
echo "   View changes: https://github.com/mirrornode/mirrornode-index/commits/main"
