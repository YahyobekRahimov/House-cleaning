import React from "react";
import { ReactComponent as EmailIcon} from '../icons/email.svg';
import { ReactComponent as PasswordIcon } from '../icons/password.svg';

function LoginForm() {
    return (
        <section>
            <div className="container userContactInfo">
                <h2 className="userContactInfo__title">Kirish uchun ma'lumotlaringizni kiriting</h2>
                <form action="/endpoint" method="post">
                    <div className="user-login-form-input">
                        <EmailIcon />
                        <input type="text" name="email" id="email" placeholder="Email" />
                    </div>
                    <div className="user-login-form-input">
                        <PasswordIcon />
                        <input type="text" name="password" id="password" placeholder="Parolni kiriting" />
                    </div>
                    <input type="submit" value="Kirish" id="submit-button" />
                </form>
            </div>
        </section>    
    )
}

export default LoginForm;