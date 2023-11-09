import {ReactComponent as LogoIcon} from '../icons/toza-makon-icon.svg'
import {ReactComponent as LogoText} from '../icons/toza-makon.svg'

function Footer() {
    return <footer className="footer">
    <div className="container footer__container">
        <div className="footer__cta">

            <p className="footer__cta__subtitle">
                Biz uchun
            </p>
            <h2 className="footer__cta__title">
                Yana savollaringiz bormi?
            </h2>
            <p className="footer__cta__description">
                Sizni qiynayotgan savollaringiz bo’lsa biz bilan bog’laning! Mutaxassislarimiz sizning
                savollaringizga javob
                berishadi!
            </p>
            <button className="footer__cta__button common-button">
                Buyurtma qilish
            </button>
        </div>

        <a className="footer__logo" href="#">
            <LogoIcon />
            <LogoText />
            <span className="slogan">Tozalik biz bilan boshlanadi</span>
        </a>

    </div>
</footer>
}

export default Footer;