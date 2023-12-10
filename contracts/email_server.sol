pragma solidity ^0.8.7;

contract Email_server {
    struct Mail {
        string sender;
        string hash;
        string web;
        string to;
    }

    event external_mail(string to, string subject, string content, string from);

    function isLowercase(string memory input) private returns (bool) {
        bytes memory inputBytes = bytes(input);
        for (uint256 i = 0; i < inputBytes.length; i++) {
            if (!(uint8(inputBytes[i]) >= 97 && uint8(inputBytes[i]) <= 122)) {
                return false;
            }
        }
        return true;
    }
    Mail[] emails;
    mapping (string=>Mail[]) user_mails;
    mapping(string=>Mail[]) sent;
    function recv_mail(string memory sender ,string memory hash, string memory web, string memory to) public {
        emails.push(Mail(sender, hash, web, to));
        user_mails[to].push(emails[emails.length-1]);
    }
    function send_mail(string memory sender ,string memory hash, string memory web, string memory to) public {
        if (isLowercase(sender)) {
            sent[sender].push(Mail(sender, hash, web, to));
        }
    }
    function get_all_mails() public view returns (Mail[] memory) {
        return emails;
    }
    function send_web2_mail(string memory to, string memory subject, string memory content, string memory from) public {
        emit external_mail(to, subject, content, from);
        sent[from].push(Mail(from, content, "web2", to));
    }
}