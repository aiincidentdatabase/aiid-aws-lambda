# aiid-aws-lambda

This repository presents AWS lambda functions that are useful in servicing the [AI Incident Database](https://github.com/PartnershipOnAI/aiid). At present it is a proof of concept useful for parsing third-party websites. Future versions may add additional endpoints.

## Current Functionality

The current functionality is for parsing news stories and returning the news stories to the client. It is configured to accept CORS requests in the Lambda API.

## Example invocation

The current API can be evoked as follows.

    const urlToEncode = "https://seanbmcgregor.com/DeepfakeDetectionGame.html";
    const encodedURL = encodeURIComponent(urlToEncode);
    const baseUrl = "https://z14490usg0.execute-api.us-east-1.amazonaws.com/default/parseNews?url=";
    const requestUrl = baseUrl + encodedURL;
    const httpRequest = new XMLHttpRequest();

    httpRequest.open("GET", requestUrl);
    httpRequest.send();

    Http2.onreadystatechange = (e) => {
      console.log(JSON.parse(httpRequest.responseText));
    }

This should result in logging an object with the following values,

    {
        authors: []
        date_download: "2021-03-10 07:16:27"
        date_modify: null
        date_publish: "2019-12-11 00:00:00"
        description: null
        filename: "https%3A%2F%2Fseanbmcgregor.com%2FDeepfakeDetectionGame.html.json"
        image_url: "https://seanbmcgregor.com/DeepfakeDetectionGame.html"
        language: "en"
        localpath: null
        maintext: "The main text of the article would go here. It is shortened here because the text is too long"
        source_domain: "seanbmcgregor.com"
        text: null
        title: "Deepfake Detection Game"
        title_page: null
        title_rss: null
        url: "https://seanbmcgregor.com/DeepfakeDetectionGame.html"
    }

Note that the library is imperfect. It failed to parse any authors.
