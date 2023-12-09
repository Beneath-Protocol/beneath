pragma solidity ^0.8.7;

contract Email_server {
    struct Mail {
        string sender;
        string hash;
        
    }
    Mail[] emails;
    function recv_mail(string memory sender ,string memory hash) public {
        emails.push(hash);
    }
}