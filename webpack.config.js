const path = require('path');


module.exports = {
    entry: {
        app: './static/js/app.js'
    },
    output: {
        path: path.resolve(__dirname, 'static/js/build'),
        filename: 'app.js'
    },
    node: {fs: 'empty'},
    module: {
        rules: [{
            test: /\.js?$/,
            exclude: /node_module/,
            loader: 'babel-loader',
            query: {
                presets: ['react', 'env', 'stage-0'],
                plugins: ['react-html-attrs', 'transform-class-properties', 'transform-decorators-legacy']
            }
        }]
    },
    devServer: {
        port: 8082,
        contentBase: 'static',
        allowedHosts: [
            '127.0.0.1',
            '0.0.0.0',
            'localhost'
        ]
    }
}
