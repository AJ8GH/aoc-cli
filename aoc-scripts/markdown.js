const TurndownService = require('turndown');
const fetch = require('node-fetch');

const year = process.argv[2];
const day = process.argv[3];
const session = process.argv[4];

const url = `https://adventofcode.com/20${year}/day/${day}`
const opts = {
    headers: {
        cookie: `session=${session}`
    }
};

const getHtml = async () => {
    const response = await fetch(url, opts);
    const html = await response.text();
    return html;
}

const html = getHtml();
const td = new TurndownService();
const markdown = html.then(result => td.turndown(result));

const arr = [];
markdown.then(md => {
    console.log(md);
    arr[0] = md;
});

return arr[0];
