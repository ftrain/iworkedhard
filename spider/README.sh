#!/bin/bash

# We want to download some websites from the Internet archive. They
# are:

# Already got Gothamist

for URL in "dnainfo.com" "dcist.com" "laist.com" "chicagoist.com" "sfist.com" "shanghaiist.com";

	   # We will use this program, it seems fine:
	   # https://github.com/hartator/wayback-machine-downloader

	   # Some probing shows that the Internet Archive is cool with
	   # about 3 concurrent connections but after that you're
	   # pushing it.

	   # We also really only want HTMLish files. The easiest way
	   # to find those is by exclusion so we just elimate any
	   # images, CSS, JS, etc. The other thing we want to avoid
	   # are articles that have querystrings at the end so we also
	   # avoid "?"

do wayback_machine_downloader ${URL} \
			      --directory /Users/ford/Dropbox/mirror/${URL} \
			      --concurrency 3 \
			      --exclude "/\?|\.(gif|jpg|jpeg|png|js|mp4|mov|flv|avi|css|pdf)$/i";
done;

# That's all.
# We are done so now we can make a database and a website.
