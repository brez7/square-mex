# Square - Premium Bootstrap Theme

## Prerequisites

```
Node.js
```

## Installing

```
npm install
```

### Gulp
#### Running in dev mode with Browsersync watch

It will run a local dev server `http://localhost:3000` and open the first page `http://localhost:3000/index.html`.
Any changes in the code will reload the page immediately. It will generate the code into `temp` folder.
```
gulp
```

#### Running in dev mode without watch

It will generate the code into `temp` folder

```
gulp dev
```

#### Production mode

It will generate a dist folder with minified js, css, html files.

```
gulp prod
```
### Laravel Mix (Webpack wrapper)
#### Running in dev mode with Browsersync watch

It will run a local dev server `http://localhost:3000` and open the first page `http://localhost:3000/index.html`.
Any changes in the code will reload the page immediately. It will generate the code into `temp` folder.
```
npm run watch
```

#### Running in dev mode without watch

It will generate the code into `temp` folder

```
npm run dev
```

#### Production mode

It will generate a dist folder with minified js, css, html files.

```
npm run production
```
#### Push to Firebase

firebase deploy

 




docker run -p 8080:8080 switch-el-test





docker build -t switch-el-test .

docker tag switch-el-test gcr.io/upbeat-button-265722/switch-el:latest

docker push gcr.io/upbeat-button-265722/switch-el:latest

gcloud run deploy switch-el --image gcr.io/upbeat-button-265722/switch-el:latest --platform managed --region us-central1 --allow-unauthenticated

 


