# We will use this program, it seems fine:
# https://github.com/hartator/wayback-machine-downloader

# wayback_machine_downloader ${URL} --directory /Users/ford/Dropbox/mirror/ --concurrency 10 --exclude "/\.(gif|jpg|jpeg|js|mp4|mov|flv|avi|css|pdf)$/i"

# And we will download

for URL in "shanghaiist.com" \
	       "dcist.com" \
	       "laist.com" \
	       "chicagoist.com" \
	       "sfist.com" \
	       "dnainfo.com" \
	       "gothamist.com";
do wayback_machine_downloader ${URL} \
			      --directory /Users/ford/Dropbox/mirror/ \
			      --concurrency 10 \
			      --exclude "/\?|\.(gif|jpg|jpeg|png|js|mp4|mov|flv|avi|css|pdf)$/i";
done;
