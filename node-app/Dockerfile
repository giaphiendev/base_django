FROM node:lts as builder

WORKDIR /server-node

COPY package*.json ./

RUN npm install -g nodemon && yarn install


#RUN npm install -g nodemon && yarn install \
#  --prefer-offline \
#  --frozen-lockfile \
#  --non-interactive \
#  --production=false

COPY . .

# If you are building your code for production
# RUN npm ci --only=production

# RUN rm -rf node_modules && \
#   NODE_ENV=production yarn install \
#   --prefer-offline \
#   --pure-lockfile \
#   --non-interactive \
#   --production=true



ENV HOST=0.0.0.0
ENV NODE_ENV=development

EXPOSE 5005

CMD [ "yarn", "dev" ]
