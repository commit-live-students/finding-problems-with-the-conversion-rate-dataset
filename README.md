# Finding problems with the Conversion Rate dataset

### The Setting

The conversion rate dataset, to be found at `"./data/conversion_data.csv"` contains the following columns:

* `country` : user country based on the IP address
* `age` : user age. Self-reported at sign-in step
* `new_user` : whether the user created the account during this session or had already an account and simply came back to the site
* `source` : marketing channel source
    * `Ads`: came to the site by clicking on an advertisement
    * `Seo`: came to the site by clicking on search results
    * `Direct`: came to the site by directly typing the URL on the browser
* `total_pages_visited`: number of total pages visited during the session.
    * This is a proxy for time spent on site and engagement during the session.
* `converted`: this is our label. 1 means they converted within the session, 0 means they left
without buying anything.

The eventual task for this dataset is to predict the `converted` column. But right now we'll focus on a few preparatory tasks.

### The Task

Your task is to write a function called `detect_outliers()` that specializes detecting outliers in `age` variables!

1. Accepts the following parameters:
    - `data`: A dataframe (in this case, the conversion rate dataframe read from the csv file)
        * the dataframe should have a column called `age`
2. It should return
    - A list of values for the `age` column/variable which are deemed outliers
3. The function should raise an error if there is no column with the name `age`