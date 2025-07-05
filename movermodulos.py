import os
import shutil

# CONFIGURA ESTO:
addons_origen = r'addons'
addons_destino = r'minimal_addons'

# Lista de módulos que quieres copiar (sin espacios, solo nombres de carpeta)
modulos_a_copiar = [
    'account',
    'mail',
    'product',
    'analytic',
    'hr_org_chart',
    'base_import_module',
    'base_install_request',
    'partner_autocomplete',
    'base_setup',
    'google_gmail',
    'phone_validation',
    'portal',
    'html_editor',
    'http_routing',
    'iap',
    'sms',
    'iap_mail',
    'l10n_mx',
    'resource_mail',
    'privacy_lookup',
    'auth_signup',
    'uom',
    'stock_account',
    'stock_sms',
    'pos_hr',
    'web_editor',
    'base_import',
    'web_tour',
    'account_edi_ubl_cii',
    'snailmail_account',
    'spreadsheet_dashboard_account',
    'onboarding',
    'spreadsheet_dashboard_stock_account',
    'payment',
    'resource',
    'snailmail',
    'point_of_sale_custom',
    'web',
    'web_hierarchy',
    'web_unsplash',
    'auth_totp_mail',
    'barcodes',
    'hr',
    'l10n_mx_hr',
    'stock',
    'digest',
    'pos_sms',
    'mail_bot',
    'mail_bot_hr',
    'pos_epson_printer',
    'point_of_sale',
    'pos_online_payment',
    'spreadsheet_dashboard',
    'spreadsheet_account',
    'auth_totp_portal',
    'barcodes_gs1_nomenclature',
    'spreadsheet',
    'spreadsheet_dashboard_pos_hr',
    'base',
    'contacts',
    'bus',
    'account_payment',
    'hr_skills',
    'auth_totp',
]

# Crea el directorio destino si no existe
if not os.path.exists(addons_destino):
    os.makedirs(addons_destino)

for modulo in modulos_a_copiar:
    origen = os.path.join(addons_origen, modulo)
    destino = os.path.join(addons_destino, modulo)

    if os.path.isdir(origen):
        if os.path.exists(destino):
            print(f"[!] Módulo ya existe en destino: {modulo}")
        else:
            shutil.copytree(origen, destino)
            print(f"[✓] Copiado: {modulo}")
    else:
        print(f"[X] No encontrado: {modulo}")
