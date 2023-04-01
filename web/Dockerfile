FROM node:18-alpine AS build

# Copy and download dependencies
WORKDIR web
COPY package*.json ./
RUN npm install

########## Production ##########

FROM build as prod

COPY . .

ENTRYPOINT ["npm", "run", "build"]