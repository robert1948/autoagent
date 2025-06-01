#!/bin/bash

echo "🔐 Enter your new Heroku API key:"
read -s HEROKU_API_KEY

echo "🔧 Updating ~/.netrc..."
cat <<EOF > ~/.netrc
machine api.heroku.com
  login user
  password $HEROKU_API_KEY
machine git.heroku.com
  login user
  password $HEROKU_API_KEY
EOF

chmod 600 ~/.netrc

echo "🔧 Exporting HEROKU_API_KEY..."
echo "export HEROKU_API_KEY=$HEROKU_API_KEY" >> ~/.bashrc
export HEROKU_API_KEY=$HEROKU_API_KEY

echo "🔍 Verifying Heroku authentication..."
heroku auth:whoami

if [ $? -eq 0 ]; then
  echo "✅ Heroku authentication successful!"
else
  echo "⚠️ Authentication failed. Please double-check your API key."
fi
