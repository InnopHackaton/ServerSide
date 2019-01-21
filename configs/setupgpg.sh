cat >foo <<EOF
     %echo Generating a basic OpenPGP key
     Key-Type: RSA
     Key-Length: 4096
     Subkey-Type: ELG-E
     Subkey-Length: 4096
     Name-Real: Joe HACKATHON
     Name-Comment: SERVER
     Name-Email: hack@hack.ru
     Expire-Date: 0
     Passphrase: noperm
     # Do a commit here, so that we can later print "done" :-)
     %commit
     %echo done
EOF
gpg --batch --gen-key foo

