# College

A repository for college related stuff and the tools to manage them.

## Preview

<div align=center>
  <img alt="Slideshow showing highlights of produced documents" src="https://github.com/sujaldev/college/assets/75830554/a47f3685-ec13-4dff-aaed-03cc6d05349c">
</div>

## Website Setup Instructions

Install the apache web server and python3 (only required for building the markdown script).

### Document Root

* Create a directory to serve as the document root, this guide assumes this to be `/var/www/ipu/`.
* Clone this repository and copy the contents of `utils/web/apache-theme/src/` to `/var/www/ipu/theme/`
* Copy `utils/web/apache-theme/.htaccess` to `/var/www/ipu/`.

### Markdown Renderer

Go to the cloned repository path and install requirements and `pyinstaller`, then do:

```bash
cd utils/web/markdown
pyinstaller --onefile --name ipu-md renderer.py
sudo mv dist/ipu-md /usr/bin/
mv template.jinja2 /var/www/ipu/theme/
```

### Apache Config

Enable these modules: `ext_filter`, `cache`, `cache_socache`, `socache_shcmb` and `mod_rewrite`. Then add the
following to your apache config:

```apacheconf
DocumentRoot /var/www/ipu

ExtFilterDefine md-to-html mode=output intype=text/markdown outtype=text/html \
    cmd="/usr/bin/ipu-md /var/www/html/theme/template.jinja2"

<Directory /var/www/ipu>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
        <If "%{QUERY_STRING} !~ /raw=True/">
                SetOutputFilter md-to-html
                AddType text/markdown .md .py .r .c .tex # add more if you want
        </If>
</Directory>
<Directory /var/www/ipu/theme>
        Options -Indexes
</Directory>

CacheSocache shmcb
CacheSocacheMaxSize 102400
CacheEnable socache /
```

---

## Related repositories

Other repositories containing college related work.

- [Proposal for the Computer Science & Systems Administration Club](https://github.com/sujaldev/cssac-proposal)
- [USAR Notice Mailing List](https://github.com/sujaldev/usar-notice-mailing-list)
