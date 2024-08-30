import { createI18n } from "vue-i18n";
import pt_br from './pt_br.json';
import en_us from './en_us.json';

export type AvailableLanguages = 'en_us' | 'pt_br';

export const i18nApplication = createI18n({
    legacy: false,
    locale: 'pt_br',
    messages: {
        pt_br: pt_br,
        en_us: en_us
    }
})

export const changeLanguage = (locale: AvailableLanguages) => {
  i18nApplication.global.locale.value = locale;  
};