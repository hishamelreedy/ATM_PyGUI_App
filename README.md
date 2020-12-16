# ATM_GUI_Desktop_Application_Demo
<h2>Main Screen</h2>
<ol>
<li>The system asks the user to enter his account number & then click enter</li>
<li>If the account number is not identified by the system, the system should show an error message then reset</li>
<li>After the user enters the correct account  
</ol>
<h2>Cash with draw</h2>
<ol>
<li>When the user choose the cash with draw system, the system would ask the user to enter the desired amount to withdraw, if the balance covers this amount of balance, the system would call function"ATM_Actuator_Out" which will provide the money to the client from the ATM outlet.</li>
<li>After the withdraw operation, the system shall print a thank you message and return to the home page.</li>
<li>Maximum allowed value per transaction is 5000 LE</li>
<li>The allowed values are multiple of 100L.E, otherwise the system shall print not allowed value and ask the user to re-enter the value</li>
<li>If the balance cannot cover the withdraw value, the system shall print a message to the user no sufficient balance</li>
</ol>
<em>Code Files are Withdraw.py & withdraw_support.py</em>
<h2>Balance Inquiry</h2>
When the user chooses this option, the system shall print a message to the user telling him no sufficient balance then the system shall go to the homepage.<br/>
<em>Code Files are: balanceinquiry.py & balanceinquiry_support.py</em>
<h2>Password Change</h2>
when the user chooses this option, the system shall ask the user to enter the new password <b>twice</b>. The system shall accept only a password with a length <b>four</b>. The two passwords shall be <b>matched</b> in order to be saved. Otherwise the system would ask the user to repeat the operation.<br/>
<h2>Fawry Service</h2>
The system provides 4 Fawry services which are:<br/>
<ol>
<li>Orange Recharge</li>
<li>Etisalat Recharge</li>
<li>Vodafone Recharge</li>
<li>We Recharge</li>
</ol> 
After the user chooses an option, the system would ask the user to enter the phone number and the amount of recharge. If the user balance would cover this operation, it would be done and the balance would be updated. If not the system would print no sufficient balance and then go to homepage.<br/> 
<em>Code Files are: fawryservice.py & fawryservice_support.py</em>