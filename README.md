# Twitter timeline grab

log_errorcheck.py runs through the log.txt file produced by collect.py and outputs Twitter accounts that encountered an error.

collect.py and tweet_collector.py are revisions of the original forked from Fridolin Linder's github ([flinder](https://github.com/flinder)). It takes Twitter IDs instead of usernames.

## Usage

Fill in your Twitter credentials, output file path and list of Twitter user IDs in
`collect.py`. 

Run with: 

```{bash}
python collect.py
```
