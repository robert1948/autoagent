FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:20

# Install any global tools if needed (e.g., yarn, eslint)
RUN npm install -g create-react-app
