ip=$(curl ifconfig.me)
touch ./ip.txt
old_ip=$(cat ./ip.txt)

if [ "$ip" != "$old_ip" ]; then 
    echo $ip
    echo $ip > ./ip.txt
    python send_mail.py -c ./.config.json --to pure.virtual@yahoo.com --subj "Got new IP address: $ip" --body ""
fi
