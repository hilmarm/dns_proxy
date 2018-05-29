python-dev:
  pkg.latest

python-pip:
  pkg.latest

python modules:
  pip.installed:
    - pkgs:
      - dnslib
      - IPy
  require:
    - pkg: python-pip
