#!/bin/bash

# Script: setup-heroku.sh
# Purpose: Set up Heroku CLI in Codespaces using API key authentication
# Usage:
#   chmod +x scripts/setup-heroku.sh
#   ./scripts/setup-heroku.sh

# 🚀 Prompt user for Heroku API key
echo "🔐 Please enter your Heroku API key (you can find it at https://dashboard.heroku.com/account):"
read -s HEROKU_API_KEY

# 📝 Export HEROKU_API_KEY as environment variable
echo "🔧 Exporting HEROKU_API_KEY to your environment..."
echo "export HEROKU_API_KEY=$HEROKU_API_KEY" >> ~/.bashrc
source ~/.bashrc

# 🔧 Create/update .netrc file for Heroku CLI authentication
echo "🔧 Setting up .netrc for Heroku authentication..."
cat <<EOF >> ~/.netrc
machine api.heroku.com
  login user
  password $HEROKU_API_KEY
machine git.heroku.com
  login user
  password $HEROKU_API_KEY
EOF

# 🔒 Set permissions for .netrc to protect credentials
chmod 600 ~/.netrc

# 🔍 Test Heroku CLI authentication
echo "🔍 Testing Heroku authentication..."
heroku auth:whoami

if [ $? -eq 0 ]; then
  echo "✅ Heroku CLI is authenticated and ready to use!"
else
  echo "⚠️ Authentication failed. Please check your API key."
fi
