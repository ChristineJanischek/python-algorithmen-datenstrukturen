FROM node:20-alpine

WORKDIR /workspace/apps/web

COPY apps/web/package*.json /workspace/apps/web/
RUN npm ci

COPY . /workspace

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]