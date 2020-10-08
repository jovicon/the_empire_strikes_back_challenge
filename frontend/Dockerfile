FROM node:12.16-alpine3.11 as build-stage

WORKDIR /app

# copiando archivo .env
COPY .env.example .env

COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build


# etapa de producción
FROM nginx:1.13.12-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html

# Add nginx config
COPY --from=build-stage /app/Docker/default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]