import lighthouse from '@lighthouse-web3/sdk'

const apiKey = "58ead955.f4b255239e91473fb86ad378b23f4f36"

import express from 'express'

const app = express()
const port = 4000

app.get('/', async (req, res) => {
    try {
        const response = await lighthouse.uploadText(req.query.data, apiKey)
        res.send(response["data"]["Hash"])
    } catch {
        res.send({"error":"101"})
    }
})

app.listen(port, () => {
    console.log(`Lightouse listening on port ${port}`)
})