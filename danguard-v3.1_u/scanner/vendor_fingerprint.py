FINGERPRINTS = {
    ".azurewebsites.net": {
        "service_name": "Azure App Service",
        "status_codes": [404],
        "content_strings": ["The resource you are looking for has been removed", "Error 404 - Web app not found"]
    },
    ".s3.amazonaws.com": {
        "service_name": "AWS S3",
        "status_codes": [404],
        "content_strings": ["<Code>NoSuchBucket</Code>"]
    },
    ".herokudns.com": {
        "service_name": "Heroku",
        "status_codes": [404],
        "content_strings": ["no such app"]
    },
    ".github.io": {
        "service_name": "GitHub Pages",
        "status_codes": [404],
        "content_strings": ["There isn't a GitHub Pages site here."]
    },
    ".netlify.app": {
        "service_name": "Netlify",
        "status_codes": [404],
        "content_strings": ["Not found"]
    },
    ".vercel.app": {
        "service_name": "Vercel",
        "status_codes": [404],
        "content_strings": ["404: NOT_FOUND"]
    }
}