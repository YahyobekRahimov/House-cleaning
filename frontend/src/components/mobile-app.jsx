import {ReactComponent as GooglePlayIcon} from '../icons/google-play.svg';
import {ReactComponent as AppStoreIcon} from '../icons/app-store.svg';

import Iphone15Pro1x from '../images/iphone-15-1x.png';
import Iphone15Pro2x from '../images/iphone-15-2x.png';
import Iphone15Pro3x from '../images/iphone-15-3x.png';

function Iphone15Pro() {
    <picture>
            <source media="(min-width: 1200px)" srcSet={Iphone15Pro3x} />

            <source media="(min-width: 800px)" srcSet={Iphone15Pro2x} />

            <img src={Iphone15Pro1x} alt="iphone 15 pro" />
    </picture>
}


function MobileApp() {
    return (
        <section class="mobile-app">
            <div class="container mobile-app__container">

                <div class="mobile-app__intro">
                    <p class="mobile-app__subtitle">
                        Biz siz uchun
                    </p>
                    <h2 class="mobile-app__title">
                        Ilovamizdan foydalanib ko’ring!
                    </h2>
                    <p class="mobile-app__description">
                        Ilovamizni hoziroq yuklab oling va u orqali xizmatlarimizdan tez va oson foydalaning.
                    </p>
                    <div class="google-apple-button-group">
                        <a href="#">
                            <GooglePlayIcon />
                        </a>
                        <a href="#">
                            <AppStoreIcon />
                        </a>
                    </div>

                </div>

            <Iphone15Pro />

            </div>
        </section>
    )
}

export default MobileApp;