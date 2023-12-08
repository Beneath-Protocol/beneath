pragma solidity ^0.8.12;

contract Central {
    struct User {
        string username;
        address owner;
        string domain;
    }
    struct Domain {
        string username;
        address owner;
        string blockchain;
        string server;
    }
    
    mapping(string=>Domain) all_domains;
    mapping(string => User) all_users;
    mapping(string => User[]) domain_users;
    function isLowercase(string memory input) private returns (bool) {
        bytes memory inputBytes = bytes(input);
        for (uint256 i = 0; i < inputBytes.length; i++) {
            if (!(uint8(inputBytes[i]) >= 97 && uint8(inputBytes[i]) <= 122)) {
                return false;
            }
        }
        return true;
    }
    function add_domain(string memory domain, string memory chain_id, string memory hash) public {
        if (keccak256(bytes(all_domains[domain].username))==keccak256("")) {
            if (isLowercase(domain)) {
                all_domains[domain]=Domain(domain, msg.sender, chain_id, hash);
            }
        }
    }
    function add_user(string memory domain, string memory username, address owner) public {
        if (all_domains[domain].owner==msg.sender) {
            if (isLowercase(domain) && isLowercase(username)) {
                all_users[string(bytes.concat(bytes.concat(bytes(username),"@"),bytes(domain)))]=User(username, owner, domain);
                domain_users[domain].push(User(username, owner, domain));
            }
        }
    }
    function get_domains(string memory domain) public view returns (Domain memory) {
        return all_domains[domain];
    }
    function get_user(string memory user) public view returns (User memory) {
        return all_users[user];
    }
}