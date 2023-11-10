import React from "react";
import { ReactComponent as UserIcon } from '../icons/profile.svg';
import { ReactComponent as PhoneCall } from '../icons/phoneCall.svg';

function UserContactInfo() {
    return (
        <>
        <section className="background-blur">
            <div className="container userContactInfo">
                <h2 className="userContactInfo__title">Aloqa ma'lumotlari</h2>
                <p className="userContactInfo__description">Aloqaga chiqishimiz uchun quyida so'ralgan ma'lumotlarni bizga jo'nating</p>
                <form action="/endpoint" method="post">
                    <div className="user-contact-form-input">
                        <UserIcon />
                        <input type="text" name="name" id="name" placeholder="Isminging" />
                    </div>
                    <div className="user-contact-form-input">
                        <PhoneCall />
                        <input type="text" name="phoneNumber" id="phoneNumber" placeholder="Telefon raqamingiz" />
                    </div>
                    <input type="submit" value="Yuborish" id="submit-button" />
                </form>
            </div>
        </section>
        </>

    )
}

export default UserContactInfo;