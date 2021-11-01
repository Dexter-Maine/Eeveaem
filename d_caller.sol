pragma solidity ^0.4.11;


contract d_caller {
 address addr;
 function d_caller() {
      addr = 0x2badaf6b2edbbfa1ea0e5c5daa2993525f2dcd78;
    }
 function send() payable {
        addr.send(this.balance / 2); // send all of the ether to the addr mentioned 
    }
 function () payable {

 }
}