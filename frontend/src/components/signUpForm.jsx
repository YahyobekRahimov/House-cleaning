import React from "react";
import { ReactComponent as EmailIcon} from '../icons/email.svg';
import { ReactComponent as PasswordIcon } from '../icons/password.svg';

function SignUp() {
    return (
        <section>
            <div className="container userContactInfo">
                <h2 className="userContactInfo__title">Ro'yxatdan o'tish uchun ma'lumotlaringizni kiriting</h2>
                <form action="/endpoint" method="post">
                    <div className="user-registration-form-input">
                        <EmailIcon />
                        <input type="text" name="email" id="email" placeholder="Email" />
                    </div>
                    <div className="user-registration-form-input">
                        <PasswordIcon />
                        <input type="text" name="password" id="password" placeholder="Parolni kiriting" />
                    </div>
                    <div className="user-registration-form-input">
                        <PasswordIcon />
                        <input type="text" name="repassword" id="repassword" placeholder="Parolni qaytadan kiriting" />
                    </div>
                    <input type="submit" value="Ro'yxatdan o'tish" id="submit-button" />
                </form>
            </div>
        </section>    
    )
}

export default SignUp;