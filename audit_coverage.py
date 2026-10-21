#!/usr/bin/env python3
"""Every user-facing surface in Cora Mobile and Cora Max maps to a help page.

⛔ WHY THIS EXISTS. The guide was extended four times on 2026-09-08 because
each pass documented the features someone happened to notice. The owner's
"I don't think you are missing only a few pages" was right both times he said
it. Noticing does not scale; enumerating does.

This walks the two Flutter trees for every screen, sheet, modal and dialog,
and asserts each one is either mapped to a page or explicitly excluded with a
reason. A NEW surface added to either app fails this until it is routed.

    python3 audit_coverage.py          # report
    python3 audit_coverage.py --strict # non-zero if anything is unrouted

Options (used by the private prepare step, see help-src/README.md):
    --src DIR        the help source to check routes against (default help-src/)
    --repo DIR       the app repo holding mobile/lib and cora-max/lib (default ..)
    --manifest JSON  extra {"map": {...}, "excluded": {...}} entries kept outside
                     this repo, for surfaces whose help is not published
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _opt(name: str, default: Path | None) -> Path | None:
    if name in sys.argv:
        i = sys.argv.index(name)
        if i + 1 >= len(sys.argv):
            raise SystemExit(f"⛔ {name} needs a value")
        return Path(sys.argv[i + 1]).resolve()
    return default


REPO = _opt("--repo", ROOT.parent)
SRC = _opt("--src", ROOT / "help-src")
MANIFEST = _opt("--manifest", None)

# surface stem -> help page slug
MAP = {
    # ── entry, profile, shell ──
    "splash": "mobile-setup", "login": "mobile-account", "register": "mobile-setup",
    "verify_email": "mobile-account", "onboarding": "mobile-setup",
    "demo_reef": "mobile-setup", "trial_intro": "mobile-plans",
    "tank_setup_wizard": "mobile-tank-profile", "tank_profile": "mobile-tank-profile",
    "guided_profile": "mobile-tank-profile", "main_shell": "mobile-tour",
    # ── dashboard ──
    "dashboard": "mobile-dashboard", "tank_live": "mobile-dashboard",
    "tank_dashboard": "max-tour", "reef_room": "max-reef-room",
    "tank_dashboard_editor": "mobile-dashboard-editing",
    "dashboard_editor": "max-dashboard-editing",
    "cm_dashboard_editor": "max-dashboard-editing",
    "dashboard_preset": "mobile-dashboard-editing",
    "cm_widget_config": "mobile-widgets", "dashboard_widget_config": "mobile-widgets",
    # ── a parameter ──
    "metric_detail": "mobile-metric-detail", "metric_readings": "mobile-metric-detail",
    "history_chart": "max-intelligence", "manual_entry_sanity": "mobile-metric-detail",
    "manual_log": "max-records", "dosing_calculator": "mobile-dosing",
    # ── devices ──
    "device_workspace": "mobile-devices", "devices": "max-devices",
    "device_health": "max-devices", "cm_device": "max-setup",
    "aquawiz_add": "mobile-connections", "gizwits_add_device": "mobile-connections",
    "provisioning": "max-setup", "pairing": "max-setup",
    "apex_dashboard": "mobile-device-control", "apex_detail": "max-device-control",
    "reefbeat_device_detail": "mobile-device-control",
    "trident_detail": "mobile-device-control", "dos_detail": "mobile-device-control",
 "gizwits_control": "mobile-device-control",
    "gizwits_ble_device": "mobile-device-control",
    "gizwits_undrivable_device": "mobile-device-control",
 "gizwits_schedule": "mobile-schedules",
    "gizwits_apply_program": "mobile-schedules", "gizwits_copy_schedule": "mobile-schedules",
    "probe_mapping": "mobile-probes", "record_probe_care": "mobile-probes",
    "consumable_alert": "mobile-consumables",
    "polling_primary": "mobile-multi-device", "voice_responder": "mobile-multi-device",
    # ── control ──
    "outlets_feed": "max-controls", "outlet_toggle": "max-controls",
    # ── alerts ──
    "alert_config": "mobile-alerts", "notification_list": "mobile-notifications",
    "notification_inbox": "max-alerts", "tank_alert_thresholds": "max-alerts",
    "threshold_edit": "max-alerts",
    # ── records ──
    "journal": "mobile-journal", "photo_viewer": "mobile-journal",
    "livestock": "mobile-livestock", "livestock_item_detail": "mobile-livestock",
    "maintenance": "mobile-maintenance", "tank_activity": "mobile-activity",
    "tank_timeline": "mobile-activity", "vacation": "mobile-vacation",
    "tank_snapshot": "mobile-sharing",
    # ── automation ──
    "automation_list": "mobile-automation", "automation_builder": "mobile-automation",
    # ── assistant ──
    "reef_assistant": "mobile-assistant", "ai_memory": "mobile-assistant",
    "ai_consent": "mobile-assistant", "assistant_rating_reason": "mobile-assistant",
    "wake_diagnostics": "max-voice",
    # ── intelligence ──
    "intelligence": "mobile-icp-health", "icp_report": "mobile-icp-health",
    "icp_trends": "mobile-icp-health", "icp": "max-intelligence",
    "health_report": "mobile-icp-health", "health_reports": "max-intelligence",
    "daily_health": "mobile-reef-buddy", "reef_buddy": "mobile-reef-buddy",
    "cycling_journey": "mobile-journeys", "issue_journey": "mobile-journeys",
    "cycling_guide": "mobile-journeys", "cycling_log": "mobile-journeys",
    # ── settings, plans, data ──
    "settings": "mobile-settings", "settings_hub": "max-settings",
    "tank_settings": "max-settings", "wifi_manager": "max-settings",
    "dosing_products": "mobile-dosing", "feedback_report": "mobile-support",
    "paywall": "mobile-plans", "redeem_code": "mobile-plans",
    "ota": "max-updates", "recovery": "max-updates",
    # ── added 2026-09-27 with the help rewrite (I18N-05 / help round) ──
    "about": "max-settings", "help_support": "max-settings",
    "answering_device": "max-voice", "language_settings": "max-settings",
    "tank_units": "max-settings", "units_settings": "mobile-settings",
    "dos_head_config": "max-device-control",
    "scene_list": "max-automation", "scene_editor": "max-automation",
    "scene_confirm": "max-automation",
    # -- added 2026-09-30 with the probe mapping v2 round --
    "metric_source": "mobile-probes", "rename_metric": "mobile-probes",
    # -- added 2026-10-01 with the phone Devices consolidation (one Add Device) --
    "brand_picker": "mobile-devices",
    "apex_setup": "mobile-connections",
    "reefbeat_setup": "mobile-connections",
    "apex_device_detail": "mobile-device-control",
    "aquawiz_device_detail": "mobile-device-control",
    "specto_device_detail": "mobile-device-control",
    # -- added 2026-10-12 with the Sept/Oct features --
    "device_rename": "mobile-devices",
    "dashboard_ai_design": "mobile-dashboard-editing",
    "feeding_routine": "mobile-journal",
    "feeding_exception": "mobile-journal",
    "insight_evidence": "mobile-reef-buddy",
    "lab_emails": "mobile-icp-health",
    "reefdose_dosing_view": "mobile-device-control",
    "reefdose_slot_redirect": "mobile-device-control",
}

# surface stem -> why it is deliberately NOT in the guide
EXCLUDED = {
    "dashboard_template": "rule templates not public yet; document when phone 350 / Cora Max OTA ships",
    "admin_dashboard": "internal admin", "admin_intelligence": "internal admin",
    "admin_partner_campaigns": "internal admin", "admin_user_detail": "internal admin",
    "admin_verify": "internal admin",
    "specto_live": "Specto is off public surfaces",
    "flo_control": "Flo is off public surfaces",
    "flo_list": "Flo is off public surfaces",
    "zigbee_button_config": "needs a gateway outside the public lineup",
    "gizwits_ble_probe": "developer probe screen",
    "webrtc_probe": "developer probe screen",
    "bounded": "layout infrastructure, not a screen",
    "admin_fleet_health": "internal admin",
}

PAT = re.compile(r"_(screen|sheet|modal|dialog|page)$")


def surfaces():
    out = {}
    for tree in ("mobile/lib", "cora-max/lib"):
        base = REPO / tree
        if not base.exists():
            raise SystemExit(f"⛔ {tree} not found from {REPO}")
        for f in base.rglob("*.dart"):
            stem = f.stem
            if PAT.search(stem):
                out.setdefault(PAT.sub("", stem), set()).add(tree.split("/")[0])
    return out


def main() -> int:
    if MANIFEST is not None:
        extra = json.loads(MANIFEST.read_text(encoding="utf-8"))
        clash = sorted((MAP.keys() & extra.get("map", {}).keys())
                       | (EXCLUDED.keys() & extra.get("excluded", {}).keys()))
        if clash:
            print(f"⛔ the manifest repeats entries already in this file: {clash}")
            return 2
        MAP.update(extra.get("map", {}))
        EXCLUDED.update(extra.get("excluded", {}))
    pages = {p.stem for p in SRC.glob("*.md") if p.name != "README.md"}
    # ⭐ Owner, 2026-10-14: Beta features are HIDDEN on the public guide. Their
    # pages carry `beta: true` and are not built, but they still exist in
    # help-src/ and still document the surface, so a surface routed to one
    # COUNTS AS ROUTED (it is reported separately below, not as a gap).
    hidden = {p.stem for p in SRC.glob("*.md") if p.name != "README.md"
              and re.search(r"^beta:\s*true\s*$", p.read_text(encoding="utf-8").split("\n---\n", 1)[0], re.M)}
    found = surfaces()
    # ⛔ A zero denominator is a broken run, not a clean tree.
    if len(found) < 60:
        print(f"⛔ only {len(found)} surfaces found — the scan is not reading the trees")
        return 2

    unrouted, badtarget = [], []
    for stem, trees in sorted(found.items()):
        if stem in EXCLUDED:
            continue
        page = MAP.get(stem)
        if page is None:
            unrouted.append((stem, ",".join(sorted(trees))))
        elif page not in pages:
            badtarget.append((stem, page))

    covered = len(found) - len(EXCLUDED & found.keys()) - len(unrouted)
    print(f"surfaces found      : {len(found)}")
    print(f"  routed to a page  : {covered}")
    to_hidden = sorted(s for s in found if MAP.get(s) in hidden and s not in EXCLUDED)
    print(f"    of which to a hidden Beta page: {len(to_hidden)}")
    print(f"  excluded on purpose: {len(EXCLUDED & found.keys())}")
    print(f"  UNROUTED          : {len(unrouted)}")
    print(f"help pages          : {len(pages)} ({len(hidden)} hidden Beta: {', '.join(sorted(hidden))})")
    if unrouted:
        print("\n⛔ no help page covers these surfaces:")
        for stem, tree in unrouted:
            print(f"   {stem:34} ({tree})")
    if badtarget:
        print("\n⛔ mapped to a page that does not exist:")
        for stem, page in badtarget:
            print(f"   {stem:34} -> {page}")
    stale = {s for s in EXCLUDED if s not in found}
    if stale:
        print(f"\n⚠️ exclusions for surfaces that no longer exist: {sorted(stale)}")

    # ⛔ A MAPPING TO A SURFACE THAT NO LONGER EXISTS. This is the hole that
    # made "0 unrouted" less reassuring than it reads: the audit proved every
    # surface HAS a page, but never that every mapping still has a surface.
    # `gizwits_group` sat here after Jecod grouping was removed from the
    # product — and the help page went on describing the feature, because
    # nothing pointed at the contradiction. A dead mapping is a live claim.
    stale_map = sorted(k for k in MAP if k not in found)
    if stale_map:
        print("\n⛔ mapped surfaces that no longer exist in the source tree:")
        for k in stale_map:
            print(f"   {k:34} -> {MAP[k]}  (does the page still describe it?)")

    if not unrouted and not badtarget and not stale_map:
        print("\n✅ every surface is routed, and every mapping still has a surface")
    return (
        1
        if ("--strict" in sys.argv and (unrouted or badtarget or stale_map))
        else 0
    )


if __name__ == "__main__":
    sys.exit(main())
