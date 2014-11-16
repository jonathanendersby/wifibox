WifiBox
=======

The WifiBox project aims to get inspiring content into under-serviced communities via locally stored content on low-cost WiFi portals.



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
