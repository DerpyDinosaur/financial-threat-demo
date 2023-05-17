FROM node:18-alpine AS build

# Copy and download dependencies
WORKDIR web
COPY package*.json ./
RUN npm install

########## Development ##########

FROM build as dev

COPY . .

ENTRYPOINT ["npm", "run", "preview"]

########## Production ##########

FROM build as prod

COPY . .

ENTRYPOINT ["npm", "run", "build"]