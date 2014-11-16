WifiBox
=======

The WifiBox project aims to get inspiring content into under-serviced communities via locally stored content on low-cost WiFi portals.

The hardware is a Raspberry Pi and a cheap wifi AP. The OS (Raspbian), platform (Django+Nginx) and content are stored on a single SD card. 


TODO: 
---
* Create full installation instructions for a new Raspbian WifiBox (Install nginx, django, virtualenv etc)
* Get the 3G dongle VPN working so that we can manage and monitor the box remotely.
* Add more content sources eg. Wikipedia Schools, Podcasts (preloaded and fetched via 3G, News fetched daily.
* So much more...


nginx config
============
<pre>
server {
        listen   80;
        server_name  domain.com www.domain.com;
        access_log  /var/log/wifibox.log;
        root   /srv/wifibox;

        location /media {
            autoindex on;

            if ($arg_force-download){
                set $fname $1;
                add_header Content-Disposition 'attachment; filename="$fname"';
            }
        }

        location /static {
            autoindex on;
        }

        location / {
                proxy_pass http://127.0.0.1:9000;
                proxy_set_header X-Forwarded-Host $server_name;
                proxy_set_header X-Real-IP $remote_addr;
                add_header P3P 'CP="ALL DSP COR PSAa PSDa OUR NOR ONL UNI COM NAV"';
        }

}
</pre>
