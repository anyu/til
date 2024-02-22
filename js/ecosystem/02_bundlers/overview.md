# Overview of Bundlers

A bundler is a tool that assembles JS code and dependencies to output a new JS file (eg. bundle file) ready for the web.

Bundles for production builds may want tree-shaking, lazy-loading, chunk splitting and old browser support.

## esbuild

- highly performant bundler that has a lot of traction
- can also serve as a transpiler
- includes: build command, optional config file, plugins to transform files
- features: tree shaking, minification, CLI
- used by Vite for transpiling
- sample `package.json` config:
    ```js
    "scripts": {
        "build": "rm -rf dist && node esbuild.config.js"
    }
    ```
- sample `esbuild.config.js`:
    ```js
    import esbuild from 'esbuild';
    import { sassPlugin } from "esbuild-sass-plugin";
    import babel from 'esbuild-plugin-babel';

    esbuild.build({
        entryPoints: ['src/index.js'],
        bundle: true,
        outfile: 'dist/bundle.js',
        plugins: [sassPlugin(), babel()],
    }).catch(() => process.exit(1));
    ```

## Webpack

- still the most popular bundler, a reasonable default
- includes: build script, config file, loaders to transform files, plugins
- sample `package.json` config:
    ```js
    "scripts": {
        "build": "rm -rf dist && webpack --mode development"
    }
    ```
- sample `webpack.config.js`:
    ```js
    module.exports = {
        entry: "./src/index.js", // entry point for bundler to start merge
        output: {
            filename: "bundle.js",
            path: path.resolve("dist")
        },
        module: {
            rules: [
                {
                    test: /\.(js|jsx)$/,
                    exclude: "/node-modules/",
                    use: "babel-loader"

                },
                {
                    test: /\.(scss|sass)$/,
                    // style-loader injects styles into HTML inside <script> tag
                    use: ["style-loader", "css-loader", "sass-loader"]
                }
            ]
        }
    }
    ```

## Rollup

- similar but slightly more lightweight to use than Webpack
- supposedly produces smaller bundle sizes, but also have seen folks say the opposite
- cons: has a ton of dependencies
- includes: build script,  optional config file, plugins to transform files
- used by Vite for bundling
- sample `package.json` config:
    ```js
    "scripts": {
        "build": "rm -rf dist && rollup -c"
    }
    ```
- sample `webpack.config.js`:
    ```js
    import babel from "@rollup/plugin-babel";
    import scss from "rollup-plugin-scss";

    export default {
        input: "./src/index.js",
        output: {
            file: "./dist/bundle.js",
            format: "cjs",
        },
        plugins: [
            // babel transpiles es6 to es5
            babel({ exclude: "node_modules/**" }),
            scss({ output: "styles.css" }),
        ]
    }
    ```
- outputs: `bundle.js`, `styles.css` - both need to be added to HTML

## Turbopack


## No longer as loved

- Parcel (zero config bundler based on SWC)
- Browserify
