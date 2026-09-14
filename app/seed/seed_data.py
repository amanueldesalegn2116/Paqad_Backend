"""
Seed data for Paqad prototype.
15 realistic Ethiopian public infrastructure projects with evidence,
discrepancies, verification requests, and public reports.
"""

import uuid
from datetime import date, datetime

# ---------------------------------------------------------------------------
# Fixed UUIDs so relationships are stable across re-seeds
# ---------------------------------------------------------------------------

def _id(n: int) -> str:
    return str(uuid.UUID(int=n))


# ---- Institution IDs ----
INST_ERA = _id(1)
INST_IPDC = _id(2)
INST_EEP = _id(3)
INST_ERC = _id(4)
INST_AWB = _id(5)
INST_EAE = _id(6)
INST_MOH = _id(7)
INST_TRA = _id(8)
INST_AACA = _id(9)
INST_MINT = _id(10)
INST_MOA = _id(11)
INST_SRHB = _id(12)

# ---- Project IDs ----
PROJ = {i: _id(100 + i) for i in range(1, 16)}

# ---- Evidence IDs ----
EV = {i: _id(200 + i) for i in range(1, 70)}

# ---- Discrepancy IDs ----
DISC = {i: _id(300 + i) for i in range(1, 15)}

# ---- Verification Request IDs ----
VREQ = {i: _id(400 + i) for i in range(1, 10)}

# ---- Verification Response IDs ----
VRES = {i: _id(500 + i) for i in range(1, 6)}

# ---- Public Report IDs ----
PREP = {i: _id(600 + i) for i in range(1, 12)}

# ===========================================================================
# INSTITUTIONS
# ===========================================================================
INSTITUTIONS = [
    {"id": INST_ERA, "name": "Ethiopian Roads Authority", "type": "agency", "region": "Federal", "logo_url": None},
    {"id": INST_IPDC, "name": "Industrial Parks Development Corporation", "type": "agency", "region": "Federal", "logo_url": None},
    {"id": INST_EEP, "name": "Ethiopian Electric Power", "type": "agency", "region": "Federal", "logo_url": None},
    {"id": INST_ERC, "name": "Ethiopian Railways Corporation", "type": "agency", "region": "Federal", "logo_url": None},
    {"id": INST_AWB, "name": "Amhara Water Bureau", "type": "regional", "region": "Amhara", "logo_url": None},
    {"id": INST_EAE, "name": "Ethiopian Airports Enterprise", "type": "agency", "region": "Federal", "logo_url": None},
    {"id": INST_MOH, "name": "Ministry of Health", "type": "federal", "region": "Federal", "logo_url": None},
    {"id": INST_TRA, "name": "Tigray Roads Authority", "type": "regional", "region": "Tigray", "logo_url": None},
    {"id": INST_AACA, "name": "Addis Ababa City Administration", "type": "municipal", "region": "Addis Ababa", "logo_url": None},
    {"id": INST_MINT, "name": "Ministry of Innovation and Technology", "type": "federal", "region": "Federal", "logo_url": None},
    {"id": INST_MOA, "name": "Ministry of Agriculture", "type": "federal", "region": "Federal", "logo_url": None},
    {"id": INST_SRHB, "name": "Sidama Regional Health Bureau", "type": "regional", "region": "Sidama", "logo_url": None},
]

# ===========================================================================
# PROJECTS
# ===========================================================================
PROJECTS = [
    # 1 - Verified
    {
        "id": PROJ[1], "institution_id": INST_ERA,
        "title": "Addis Ababa\u2013Adama Expressway Rehabilitation",
        "description": "Comprehensive rehabilitation of the 80 km Addis\u2013Adama expressway including resurfacing, drainage improvements, and safety barrier installation.",
        "location": "Addis Ababa to Adama", "region": "Oromia",
        "latitude": 8.56, "longitude": 39.27,
        "promised_budget": 1_200_000_000, "spent_budget": 1_150_000_000,
        "promised_output": "80 km full expressway rehabilitation",
        "current_output": "78 km completed, 2 km in final inspection",
        "announcement_date": date(2023, 3, 15), "deadline": date(2026, 6, 30),
        "status": "Verified", "progress_pct": 97.5,
    },
    # 2 - Conflicting Evidence
    {
        "id": PROJ[2], "institution_id": INST_IPDC,
        "title": "Hawassa Industrial Park Phase II",
        "description": "Expansion of the Hawassa Industrial Park with 12 new factory sheds, worker amenities, and wastewater treatment upgrade.",
        "location": "Hawassa", "region": "Sidama",
        "latitude": 7.06, "longitude": 38.48,
        "promised_budget": 850_000_000, "spent_budget": 620_000_000,
        "promised_output": "12 factory sheds and wastewater treatment plant",
        "current_output": "8 sheds built; treatment plant incomplete",
        "announcement_date": date(2023, 9, 1), "deadline": date(2026, 3, 31),
        "status": "Conflicting Evidence", "progress_pct": 55.0,
    },
    # 3 - Monitoring
    {
        "id": PROJ[3], "institution_id": INST_EEP,
        "title": "Grand Renaissance Dam Transmission Line",
        "description": "500 kV high-voltage transmission line from GERD to Addis Ababa national grid.",
        "location": "Benishangul-Gumuz to Addis Ababa", "region": "Benishangul-Gumuz",
        "latitude": 11.21, "longitude": 35.09,
        "promised_budget": 2_400_000_000, "spent_budget": 1_600_000_000,
        "promised_output": "460 km transmission line with 4 substations",
        "current_output": "310 km completed, 2 substations operational",
        "announcement_date": date(2022, 7, 10), "deadline": date(2027, 12, 31),
        "status": "Monitoring", "progress_pct": 67.0,
    },
    # 4 - Verification Requested
    {
        "id": PROJ[4], "institution_id": INST_ERC,
        "title": "Addis Ababa Light Rail Extension",
        "description": "Extension of the existing Addis Ababa Light Rail Transit system with 12 km of new track and 8 stations serving the western corridor.",
        "location": "Addis Ababa", "region": "Addis Ababa",
        "latitude": 9.02, "longitude": 38.75,
        "promised_budget": 3_200_000_000, "spent_budget": 1_800_000_000,
        "promised_output": "12 km new track with 8 stations",
        "current_output": "3 km track laid; 2 stations under construction",
        "announcement_date": date(2023, 1, 20), "deadline": date(2027, 6, 30),
        "status": "Verification Requested", "progress_pct": 25.0,
    },
    # 5 - Documented
    {
        "id": PROJ[5], "institution_id": INST_AWB,
        "title": "Bahir Dar Water Treatment Plant",
        "description": "New water treatment facility to serve 500,000 residents with clean drinking water from Lake Tana.",
        "location": "Bahir Dar", "region": "Amhara",
        "latitude": 11.60, "longitude": 37.39,
        "promised_budget": 180_000_000, "spent_budget": 45_000_000,
        "promised_output": "50 ML/day treatment capacity",
        "current_output": "Site cleared; foundation work begun",
        "announcement_date": date(2024, 5, 10), "deadline": date(2027, 9, 30),
        "status": "Documented", "progress_pct": 15.0,
    },
    # 6 - Reported
    {
        "id": PROJ[6], "institution_id": INST_EAE,
        "title": "Dire Dawa Airport Modernization",
        "description": "Modernization of Aba Tenna Dejazmach Yilma International Airport including new terminal building and runway extension.",
        "location": "Dire Dawa", "region": "Dire Dawa",
        "latitude": 9.62, "longitude": 41.85,
        "promised_budget": 560_000_000, "spent_budget": 0,
        "promised_output": "New 12,000 sqm terminal and 500m runway extension",
        "current_output": None,
        "announcement_date": date(2025, 2, 15), "deadline": date(2028, 12, 31),
        "status": "Reported", "progress_pct": 0.0,
    },
    # 7 - Verified
    {
        "id": PROJ[7], "institution_id": INST_MOH,
        "title": "Jimma University Medical Center Expansion",
        "description": "Addition of 200-bed wing, upgraded surgical theater, and medical equipment procurement.",
        "location": "Jimma", "region": "Oromia",
        "latitude": 7.68, "longitude": 36.83,
        "promised_budget": 420_000_000, "spent_budget": 405_000_000,
        "promised_output": "200-bed wing and 6 surgical theaters",
        "current_output": "200 beds operational; 6 theaters equipped",
        "announcement_date": date(2022, 11, 1), "deadline": date(2025, 12, 31),
        "status": "Verified", "progress_pct": 100.0,
    },
    # 8 - Unresolved
    {
        "id": PROJ[8], "institution_id": INST_TRA,
        "title": "Mekelle\u2013Wukro Road Project",
        "description": "Construction of a 45 km all-weather road connecting Mekelle to Wukro.",
        "location": "Mekelle to Wukro", "region": "Tigray",
        "latitude": 13.50, "longitude": 39.47,
        "promised_budget": 95_000_000, "spent_budget": 70_000_000,
        "promised_output": "45 km asphalt road",
        "current_output": "28 km gravel road completed; asphalt not applied",
        "announcement_date": date(2022, 4, 1), "deadline": date(2025, 3, 31),
        "status": "Unresolved", "progress_pct": 40.0,
    },
    # 9 - Partially Verified
    {
        "id": PROJ[9], "institution_id": INST_AACA,
        "title": "Addis Ababa Riverside Green Development",
        "description": "Urban green corridor along the Kebena and Banteyiketu rivers with parks, walking paths, and flood mitigation.",
        "location": "Addis Ababa", "region": "Addis Ababa",
        "latitude": 9.01, "longitude": 38.76,
        "promised_budget": 320_000_000, "spent_budget": 210_000_000,
        "promised_output": "15 km riverside park and flood barriers",
        "current_output": "9 km park completed; flood barriers at 60%",
        "announcement_date": date(2023, 6, 15), "deadline": date(2026, 12, 31),
        "status": "Partially Verified", "progress_pct": 65.0,
    },
    # 10 - Monitoring
    {
        "id": PROJ[10], "institution_id": INST_MINT,
        "title": "National Digital ID System (Fayda)",
        "description": "Nationwide digital identity system with biometric enrollment targeting 70 million citizens.",
        "location": "Nationwide", "region": "Federal",
        "latitude": 9.02, "longitude": 38.75,
        "promised_budget": 680_000_000, "spent_budget": 340_000_000,
        "promised_output": "70 million digital IDs issued",
        "current_output": "12 million enrolled; system in pilot regions",
        "announcement_date": date(2023, 8, 1), "deadline": date(2028, 6, 30),
        "status": "Monitoring", "progress_pct": 17.0,
    },
    # 11 - Conflicting Evidence
    {
        "id": PROJ[11], "institution_id": INST_MOA,
        "title": "Gambella Agricultural Irrigation Scheme",
        "description": "Large-scale irrigation scheme on Baro River to irrigate 10,000 hectares for commercial agriculture.",
        "location": "Gambella", "region": "Gambella",
        "latitude": 8.25, "longitude": 34.59,
        "promised_budget": 145_000_000, "spent_budget": 120_000_000,
        "promised_output": "10,000 hectares irrigated farmland",
        "current_output": "Canal built; only 3,200 hectares functional",
        "announcement_date": date(2022, 2, 1), "deadline": date(2025, 8, 31),
        "status": "Conflicting Evidence", "progress_pct": 32.0,
    },
    # 12 - Documented
    {
        "id": PROJ[12], "institution_id": INST_EAE,
        "title": "Bole International Terminal Expansion",
        "description": "Major expansion of Bole International Airport with new Terminal 3, additional gates, and modernized cargo facility.",
        "location": "Addis Ababa", "region": "Addis Ababa",
        "latitude": 8.98, "longitude": 38.80,
        "promised_budget": 4_500_000_000, "spent_budget": 800_000_000,
        "promised_output": "New Terminal 3 with 60 gates and cargo hub",
        "current_output": "Design finalized; site preparation in progress",
        "announcement_date": date(2024, 11, 1), "deadline": date(2029, 12, 31),
        "status": "Documented", "progress_pct": 8.0,
    },
    # 13 - Verified
    {
        "id": PROJ[13], "institution_id": INST_EEP,
        "title": "Adama Wind Farm Phase III",
        "description": "Addition of 51 wind turbines generating 153 MW at Adama I and II sites.",
        "location": "Adama", "region": "Oromia",
        "latitude": 8.54, "longitude": 39.27,
        "promised_budget": 780_000_000, "spent_budget": 760_000_000,
        "promised_output": "153 MW installed capacity",
        "current_output": "153 MW operational and grid-connected",
        "announcement_date": date(2022, 5, 1), "deadline": date(2025, 6, 30),
        "status": "Verified", "progress_pct": 100.0,
    },
    # 14 - Verification Requested
    {
        "id": PROJ[14], "institution_id": INST_SRHB,
        "title": "Sidama Regional Referral Hospital",
        "description": "Construction of a 300-bed regional referral hospital in Hawassa to serve the Sidama region.",
        "location": "Hawassa", "region": "Sidama",
        "latitude": 7.05, "longitude": 38.47,
        "promised_budget": 210_000_000, "spent_budget": 140_000_000,
        "promised_output": "300-bed referral hospital",
        "current_output": "Building structure 85% complete; no equipment installed",
        "announcement_date": date(2023, 4, 1), "deadline": date(2026, 9, 30),
        "status": "Verification Requested", "progress_pct": 45.0,
    },
    # 15 - Monitoring
    {
        "id": PROJ[15], "institution_id": INST_ERC,
        "title": "Addis Ababa\u2013Djibouti Railway Maintenance Program",
        "description": "Comprehensive maintenance and signaling upgrade for the 756 km electrified railway.",
        "location": "Addis Ababa to Djibouti border", "region": "Federal",
        "latitude": 9.02, "longitude": 38.75,
        "promised_budget": 520_000_000, "spent_budget": 280_000_000,
        "promised_output": "Full signaling upgrade and 200 km track renewal",
        "current_output": "Signaling 60% upgraded; 120 km track renewed",
        "announcement_date": date(2024, 1, 15), "deadline": date(2027, 3, 31),
        "status": "Monitoring", "progress_pct": 54.0,
    },
]

# ===========================================================================
# EVIDENCE
# ===========================================================================
EVIDENCE = [
    # --- Project 1: Expressway (Verified) ---
    {"id": EV[1], "project_id": PROJ[1], "source": "Ethiopian Roads Authority", "source_type": "government_announcement", "evidence_date": date(2023, 3, 15), "document_title": "Addis\u2013Adama Expressway Rehabilitation Announcement", "extracted_claim": "ERA commits to full rehabilitation of 80 km Addis\u2013Adama expressway with ETB 1.2B budget.", "evidence_status": "Corroborated"},
    {"id": EV[2], "project_id": PROJ[1], "source": "ERA Quarterly Report Q2 2025", "source_type": "progress_report", "evidence_date": date(2025, 7, 1), "document_title": "ERA Progress Report Q2 2025", "extracted_claim": "78 km of resurfacing completed. Drainage and barriers installed on 75 km.", "evidence_status": "Corroborated"},
    {"id": EV[3], "project_id": PROJ[1], "source": "Independent Road Assessment Team", "source_type": "audit_report", "evidence_date": date(2026, 2, 15), "document_title": "Independent Assessment of Addis\u2013Adama Works", "extracted_claim": "Assessment confirms 78 km quality resurfacing. Remaining 2 km under final inspection.", "evidence_status": "Corroborated"},
    {"id": EV[4], "project_id": PROJ[1], "source": "Citizen Observation", "source_type": "citizen_report", "evidence_date": date(2026, 5, 20), "document_title": "Citizen Verification Report", "extracted_claim": "Road quality noticeably improved along Addis\u2013Adama corridor. New barriers visible.", "evidence_status": "Corroborated"},

    # --- Project 2: Hawassa Industrial Park (Conflicting Evidence) ---
    {"id": EV[5], "project_id": PROJ[2], "source": "IPDC Official Statement", "source_type": "government_announcement", "evidence_date": date(2023, 9, 1), "document_title": "Hawassa IP Phase II Launch", "extracted_claim": "12 factory sheds and full wastewater treatment plant to be delivered by March 2026.", "evidence_status": "Reviewed"},
    {"id": EV[6], "project_id": PROJ[2], "source": "IPDC Progress Update", "source_type": "progress_report", "evidence_date": date(2025, 6, 15), "document_title": "IPDC Mid-Year Progress Report 2025", "extracted_claim": "10 of 12 factory sheds completed. Wastewater treatment plant at 90% completion.", "evidence_status": "Contested"},
    {"id": EV[7], "project_id": PROJ[2], "source": "Environmental Impact Monitor", "source_type": "audit_report", "evidence_date": date(2025, 9, 1), "document_title": "Hawassa IP Environmental Audit", "extracted_claim": "Only 8 sheds are structurally complete. Wastewater plant foundation has significant defects requiring redesign.", "evidence_status": "Reviewed"},
    {"id": EV[8], "project_id": PROJ[2], "source": "Local Media Report", "source_type": "media_report", "evidence_date": date(2025, 10, 12), "document_title": "Hawassa Industrial Park Delays Questioned", "extracted_claim": "Workers report only 8 functional sheds. Untreated wastewater observed flowing into Lake Hawassa.", "evidence_status": "Reviewed"},
    {"id": EV[9], "project_id": PROJ[2], "source": "Citizen Photo Report", "source_type": "photo_evidence", "evidence_date": date(2025, 11, 5), "document_title": "Photo Evidence \u2013 Incomplete Sheds", "extracted_claim": "Photos show 4 shed structures without roofing or electrical installations.", "evidence_status": "Reviewed"},

    # --- Project 3: Transmission Line (Monitoring) ---
    {"id": EV[10], "project_id": PROJ[3], "source": "Ethiopian Electric Power", "source_type": "government_announcement", "evidence_date": date(2022, 7, 10), "document_title": "GERD Transmission Line Project Announcement", "extracted_claim": "460 km 500kV line with 4 substations, ETB 2.4B budget.", "evidence_status": "Reviewed"},
    {"id": EV[11], "project_id": PROJ[3], "source": "EEP Annual Report 2024", "source_type": "progress_report", "evidence_date": date(2025, 1, 15), "document_title": "EEP Annual Report 2024", "extracted_claim": "310 km of transmission line erected. 2 substations energized.", "evidence_status": "Reviewed"},
    {"id": EV[12], "project_id": PROJ[3], "source": "World Bank Mission Report", "source_type": "audit_report", "evidence_date": date(2025, 8, 1), "document_title": "WB Energy Sector Review", "extracted_claim": "Project on track for 2027 completion. Procurement delays noted for substation 3 equipment.", "evidence_status": "Corroborated"},

    # --- Project 4: Light Rail Extension (Verification Requested) ---
    {"id": EV[13], "project_id": PROJ[4], "source": "Ethiopian Railways Corporation", "source_type": "government_announcement", "evidence_date": date(2023, 1, 20), "document_title": "Light Rail Western Extension Announcement", "extracted_claim": "12 km extension with 8 new stations, ETB 3.2B budget, completion by mid-2027.", "evidence_status": "Reviewed"},
    {"id": EV[14], "project_id": PROJ[4], "source": "ERC Progress Update", "source_type": "progress_report", "evidence_date": date(2025, 4, 1), "document_title": "ERC Light Rail Progress Q1 2025", "extracted_claim": "Track laying progressing well. 5 km of track bed prepared.", "evidence_status": "Contested"},
    {"id": EV[15], "project_id": PROJ[4], "source": "Transport Analysts Report", "source_type": "media_report", "evidence_date": date(2025, 7, 20), "document_title": "Light Rail Extension Reality Check", "extracted_claim": "Site visits reveal only 3 km of track laid, significantly behind schedule. Budget concerns raised.", "evidence_status": "Reviewed"},
    {"id": EV[16], "project_id": PROJ[4], "source": "Citizen Observation", "source_type": "citizen_report", "evidence_date": date(2025, 9, 10), "document_title": "Community Report on LRT Works", "extracted_claim": "Residents report construction stopped for 3 months near Ayat area.", "evidence_status": "Reviewed"},

    # --- Project 5: Water Treatment (Documented) ---
    {"id": EV[17], "project_id": PROJ[5], "source": "Amhara Water Bureau", "source_type": "government_announcement", "evidence_date": date(2024, 5, 10), "document_title": "Bahir Dar Water Treatment Project Launch", "extracted_claim": "New 50 ML/day facility to serve 500,000 residents. ETB 180M budget.", "evidence_status": "Reviewed"},
    {"id": EV[18], "project_id": PROJ[5], "source": "AWB Budget Allocation", "source_type": "budget_report", "evidence_date": date(2024, 7, 1), "document_title": "FY 2024/25 Water Sector Budget", "extracted_claim": "ETB 45M allocated for initial phase of Bahir Dar water treatment.", "evidence_status": "Reviewed"},
    {"id": EV[19], "project_id": PROJ[5], "source": "Site Inspection Report", "source_type": "progress_report", "evidence_date": date(2025, 3, 15), "document_title": "Bahir Dar WTP Site Inspection", "extracted_claim": "Site cleared and foundation excavation at 70%. Access road constructed.", "evidence_status": "Reviewed"},

    # --- Project 6: Dire Dawa Airport (Reported) ---
    {"id": EV[20], "project_id": PROJ[6], "source": "Ethiopian Airports Enterprise", "source_type": "government_announcement", "evidence_date": date(2025, 2, 15), "document_title": "Dire Dawa Airport Modernization Plan", "extracted_claim": "New 12,000 sqm terminal and 500m runway extension planned with ETB 560M budget.", "evidence_status": "Pending Review"},

    # --- Project 7: Jimma Hospital (Verified) ---
    {"id": EV[21], "project_id": PROJ[7], "source": "Ministry of Health", "source_type": "government_announcement", "evidence_date": date(2022, 11, 1), "document_title": "Jimma Medical Center Expansion Announcement", "extracted_claim": "200-bed wing and 6 surgical theaters to be added, ETB 420M.", "evidence_status": "Corroborated"},
    {"id": EV[22], "project_id": PROJ[7], "source": "MoH Completion Report", "source_type": "progress_report", "evidence_date": date(2025, 11, 30), "document_title": "Jimma Medical Center \u2013 Project Completion Report", "extracted_claim": "200-bed wing inaugurated. All 6 theaters equipped and operational.", "evidence_status": "Corroborated"},
    {"id": EV[23], "project_id": PROJ[7], "source": "WHO Ethiopia", "source_type": "audit_report", "evidence_date": date(2026, 1, 15), "document_title": "WHO Health Facility Assessment", "extracted_claim": "Independent verification confirms 200 beds and 6 theaters fully functional.", "evidence_status": "Corroborated"},

    # --- Project 8: Mekelle Road (Unresolved) ---
    {"id": EV[24], "project_id": PROJ[8], "source": "Tigray Roads Authority", "source_type": "government_announcement", "evidence_date": date(2022, 4, 1), "document_title": "Mekelle\u2013Wukro Road Construction Announcement", "extracted_claim": "45 km asphalt road to be completed by March 2025. ETB 95M budget.", "evidence_status": "Reviewed"},
    {"id": EV[25], "project_id": PROJ[8], "source": "TRA Progress Report", "source_type": "progress_report", "evidence_date": date(2024, 12, 1), "document_title": "TRA Road Progress Report", "extracted_claim": "Road construction progressing well. 35 km of road base prepared.", "evidence_status": "Contested"},
    {"id": EV[26], "project_id": PROJ[8], "source": "Field Investigation", "source_type": "media_report", "evidence_date": date(2025, 6, 1), "document_title": "Mekelle\u2013Wukro Road Investigation", "extracted_claim": "Only 28 km of gravel road exists. No asphalt has been applied. Deadline passed.", "evidence_status": "Reviewed"},
    {"id": EV[27], "project_id": PROJ[8], "source": "Community Leaders", "source_type": "citizen_report", "evidence_date": date(2025, 8, 15), "document_title": "Wukro Community Statement", "extracted_claim": "Community reports road is still gravel, impassable during rainy season.", "evidence_status": "Reviewed"},

    # --- Project 9: Riverside Green (Partially Verified) ---
    {"id": EV[28], "project_id": PROJ[9], "source": "Addis Ababa City Administration", "source_type": "government_announcement", "evidence_date": date(2023, 6, 15), "document_title": "Riverside Green Development Launch", "extracted_claim": "15 km riverside park and flood barriers. ETB 320M investment.", "evidence_status": "Reviewed"},
    {"id": EV[29], "project_id": PROJ[9], "source": "AACA Urban Report", "source_type": "progress_report", "evidence_date": date(2025, 12, 1), "document_title": "AACA Riverside Development Update", "extracted_claim": "9 km of walking paths and green spaces completed. Flood barriers under construction.", "evidence_status": "Corroborated"},
    {"id": EV[30], "project_id": PROJ[9], "source": "Urban Planning Review", "source_type": "audit_report", "evidence_date": date(2026, 3, 1), "document_title": "Independent Urban Development Review", "extracted_claim": "9 km park verified as functional. Flood barrier progress at approximately 60%.", "evidence_status": "Corroborated"},

    # --- Project 10: Digital ID (Monitoring) ---
    {"id": EV[31], "project_id": PROJ[10], "source": "Ministry of Innovation and Technology", "source_type": "government_announcement", "evidence_date": date(2023, 8, 1), "document_title": "Fayda Digital ID Program Launch", "extracted_claim": "70 million citizens to receive digital IDs by 2028. ETB 680M budget.", "evidence_status": "Reviewed"},
    {"id": EV[32], "project_id": PROJ[10], "source": "MInT Progress Report", "source_type": "progress_report", "evidence_date": date(2025, 12, 31), "document_title": "Fayda Year-End Report 2025", "extracted_claim": "12 million citizens enrolled across pilot regions.", "evidence_status": "Reviewed"},
    {"id": EV[33], "project_id": PROJ[10], "source": "Digital Rights Group", "source_type": "media_report", "evidence_date": date(2026, 2, 1), "document_title": "Fayda Implementation Review", "extracted_claim": "Enrollment pace suggests target may be difficult to meet. Data protection concerns noted.", "evidence_status": "Reviewed"},

    # --- Project 11: Gambella Irrigation (Conflicting Evidence) ---
    {"id": EV[34], "project_id": PROJ[11], "source": "Ministry of Agriculture", "source_type": "government_announcement", "evidence_date": date(2022, 2, 1), "document_title": "Gambella Irrigation Scheme Announcement", "extracted_claim": "10,000 hectares to be irrigated from Baro River. ETB 145M.", "evidence_status": "Reviewed"},
    {"id": EV[35], "project_id": PROJ[11], "source": "MoA Progress Report", "source_type": "progress_report", "evidence_date": date(2024, 12, 1), "document_title": "MoA Irrigation Progress Report", "extracted_claim": "Main canal completed. 8,000 hectares prepared for irrigation.", "evidence_status": "Contested"},
    {"id": EV[36], "project_id": PROJ[11], "source": "Agricultural Monitor", "source_type": "audit_report", "evidence_date": date(2025, 3, 15), "document_title": "Gambella Irrigation Field Assessment", "extracted_claim": "Canal constructed but secondary channels incomplete. Only 3,200 hectares receiving water.", "evidence_status": "Reviewed"},
    {"id": EV[37], "project_id": PROJ[11], "source": "Local Farmers Association", "source_type": "citizen_report", "evidence_date": date(2025, 7, 1), "document_title": "Farmer Report on Irrigation Status", "extracted_claim": "Most farmland remains dry. Canal water does not reach our fields.", "evidence_status": "Reviewed"},

    # --- Project 12: Bole Terminal (Documented) ---
    {"id": EV[38], "project_id": PROJ[12], "source": "Ethiopian Airports Enterprise", "source_type": "government_announcement", "evidence_date": date(2024, 11, 1), "document_title": "Bole Airport Terminal 3 Announcement", "extracted_claim": "New Terminal 3 with 60 gates and cargo hub. ETB 4.5B investment.", "evidence_status": "Reviewed"},
    {"id": EV[39], "project_id": PROJ[12], "source": "EAE Project Document", "source_type": "official_document", "evidence_date": date(2025, 3, 1), "document_title": "Terminal 3 Design Document", "extracted_claim": "Design completed by international consortium. Site preparation authorized.", "evidence_status": "Reviewed"},
    {"id": EV[40], "project_id": PROJ[12], "source": "Aviation Weekly", "source_type": "media_report", "evidence_date": date(2025, 6, 15), "document_title": "Bole Airport Expansion Timeline", "extracted_claim": "Site preparation underway. Full construction expected to begin late 2025.", "evidence_status": "Reviewed"},

    # --- Project 13: Wind Farm (Verified) ---
    {"id": EV[41], "project_id": PROJ[13], "source": "Ethiopian Electric Power", "source_type": "government_announcement", "evidence_date": date(2022, 5, 1), "document_title": "Adama Wind Farm Phase III Announcement", "extracted_claim": "51 turbines for 153 MW capacity at Adama. ETB 780M.", "evidence_status": "Corroborated"},
    {"id": EV[42], "project_id": PROJ[13], "source": "EEP Completion Report", "source_type": "progress_report", "evidence_date": date(2025, 5, 15), "document_title": "Adama III Completion Report", "extracted_claim": "All 51 turbines installed and grid-connected. 153 MW operational capacity confirmed.", "evidence_status": "Corroborated"},
    {"id": EV[43], "project_id": PROJ[13], "source": "Energy Regulatory Authority", "source_type": "audit_report", "evidence_date": date(2025, 7, 1), "document_title": "ERA Grid Integration Audit", "extracted_claim": "153 MW verified as operational and supplying the national grid.", "evidence_status": "Corroborated"},

    # --- Project 14: Sidama Hospital (Verification Requested) ---
    {"id": EV[44], "project_id": PROJ[14], "source": "Sidama Regional Health Bureau", "source_type": "government_announcement", "evidence_date": date(2023, 4, 1), "document_title": "Sidama Regional Hospital Announcement", "extracted_claim": "300-bed referral hospital to serve the Sidama region. ETB 210M.", "evidence_status": "Reviewed"},
    {"id": EV[45], "project_id": PROJ[14], "source": "SRHB Progress Report", "source_type": "progress_report", "evidence_date": date(2025, 6, 1), "document_title": "SRHB Hospital Construction Update", "extracted_claim": "Building structure 85% complete. Equipment procurement initiated.", "evidence_status": "Contested"},
    {"id": EV[46], "project_id": PROJ[14], "source": "Health Sector Watch", "source_type": "media_report", "evidence_date": date(2025, 9, 15), "document_title": "Sidama Hospital Progress Review", "extracted_claim": "Structure appears around 70% complete. No medical equipment on site despite claims.", "evidence_status": "Reviewed"},

    # --- Project 15: Railway Maintenance (Monitoring) ---
    {"id": EV[47], "project_id": PROJ[15], "source": "Ethiopian Railways Corporation", "source_type": "government_announcement", "evidence_date": date(2024, 1, 15), "document_title": "Railway Maintenance Program Launch", "extracted_claim": "Full signaling upgrade and 200 km track renewal. ETB 520M budget.", "evidence_status": "Reviewed"},
    {"id": EV[48], "project_id": PROJ[15], "source": "ERC Semi-Annual Report", "source_type": "progress_report", "evidence_date": date(2025, 7, 1), "document_title": "Railway Maintenance Progress H1 2025", "extracted_claim": "Signaling 60% upgraded. 120 km of track renewed.", "evidence_status": "Reviewed"},
    {"id": EV[49], "project_id": PROJ[15], "source": "Transport Authority Inspection", "source_type": "audit_report", "evidence_date": date(2026, 1, 15), "document_title": "Railway Safety Inspection Report", "extracted_claim": "Signal system upgrades verified on main corridor. Track quality improved on renewed sections.", "evidence_status": "Corroborated"},
]

# ===========================================================================
# DISCREPANCIES
# ===========================================================================
DISCREPANCIES = [
    # Project 2 - Hawassa IP
    {
        "id": DISC[1], "project_id": PROJ[2],
        "official_claim": "10 of 12 factory sheds completed and wastewater treatment at 90%.",
        "supporting_evidence_id": EV[6],
        "conflicting_evidence_id": EV[7],
        "reason_flagged": "Environmental audit found only 8 sheds structurally complete and significant wastewater plant foundation defects, contradicting the official progress report.",
        "verification_status": "Under Review",
    },
    {
        "id": DISC[2], "project_id": PROJ[2],
        "official_claim": "Wastewater treatment plant at 90% completion.",
        "supporting_evidence_id": EV[6],
        "conflicting_evidence_id": EV[8],
        "reason_flagged": "Media report documents untreated wastewater flowing into Lake Hawassa, inconsistent with 90% treatment plant completion claim.",
        "verification_status": "Pending",
    },
    # Project 4 - Light Rail
    {
        "id": DISC[3], "project_id": PROJ[4],
        "official_claim": "5 km of track bed prepared for the western extension.",
        "supporting_evidence_id": EV[14],
        "conflicting_evidence_id": EV[15],
        "reason_flagged": "Independent transport analysts found only 3 km of track actually laid during site visits, contradicting the 5 km claim.",
        "verification_status": "Pending",
    },
    # Project 8 - Mekelle Road
    {
        "id": DISC[4], "project_id": PROJ[8],
        "official_claim": "35 km of road base prepared for the Mekelle\u2013Wukro corridor.",
        "supporting_evidence_id": EV[25],
        "conflicting_evidence_id": EV[26],
        "reason_flagged": "Field investigation found only 28 km of gravel road with no asphalt application despite deadline having passed.",
        "verification_status": "Unresolved",
    },
    # Project 11 - Gambella Irrigation
    {
        "id": DISC[5], "project_id": PROJ[11],
        "official_claim": "8,000 hectares prepared for irrigation from the main canal.",
        "supporting_evidence_id": EV[35],
        "conflicting_evidence_id": EV[36],
        "reason_flagged": "Field assessment shows secondary channels incomplete with only 3,200 hectares actually receiving water, a 60% shortfall from the claimed 8,000.",
        "verification_status": "Pending",
    },
    # Project 14 - Sidama Hospital
    {
        "id": DISC[6], "project_id": PROJ[14],
        "official_claim": "Building structure 85% complete and equipment procurement initiated.",
        "supporting_evidence_id": EV[45],
        "conflicting_evidence_id": EV[46],
        "reason_flagged": "Independent review estimates structure at 70% with no medical equipment visible on site, contradicting claims of procurement initiation.",
        "verification_status": "Pending",
    },
]

# ===========================================================================
# VERIFICATION REQUESTS
# ===========================================================================
VERIFICATION_REQUESTS = [
    # Project 4 - Light Rail
    {
        "id": VREQ[1], "project_id": PROJ[4], "discrepancy_id": DISC[3],
        "information_requested": "Please provide updated site photographs, surveyor reports, and contractor progress logs for the western corridor track laying as of September 2025.",
        "date_requested": date(2025, 10, 1),
        "current_state": "Pending",
    },
    # Project 2 - Hawassa IP (shed count)
    {
        "id": VREQ[2], "project_id": PROJ[2], "discrepancy_id": DISC[1],
        "information_requested": "Request for updated structural completion certificates for all 12 factory sheds and current wastewater treatment plant engineering assessment.",
        "date_requested": date(2025, 11, 15),
        "current_state": "Acknowledged",
    },
    # Project 2 - Hawassa IP (wastewater)
    {
        "id": VREQ[3], "project_id": PROJ[2], "discrepancy_id": DISC[2],
        "information_requested": "Request for environmental compliance certificate and water quality test results for treatment plant discharge.",
        "date_requested": date(2025, 11, 20),
        "current_state": "No Response",
    },
    # Project 8 - Mekelle Road
    {
        "id": VREQ[4], "project_id": PROJ[8], "discrepancy_id": DISC[4],
        "information_requested": "Request for detailed road survey data, asphalt procurement records, and revised project timeline.",
        "date_requested": date(2025, 7, 1),
        "current_state": "No Response",
    },
    # Project 11 - Gambella Irrigation
    {
        "id": VREQ[5], "project_id": PROJ[11], "discrepancy_id": DISC[5],
        "information_requested": "Request for updated irrigation coverage maps, water flow measurements, and secondary channel construction schedule.",
        "date_requested": date(2025, 8, 1),
        "current_state": "Response Received",
    },
    # Project 14 - Sidama Hospital
    {
        "id": VREQ[6], "project_id": PROJ[14], "discrepancy_id": DISC[6],
        "information_requested": "Request for structural engineer report, equipment procurement orders, and delivery timeline.",
        "date_requested": date(2026, 1, 15),
        "current_state": "Pending",
    },
]

# ===========================================================================
# VERIFICATION RESPONSES
# ===========================================================================
VERIFICATION_RESPONSES = [
    # Response for Hawassa IP shed count
    {
        "id": VRES[1], "request_id": VREQ[2],
        "response_text": "IPDC acknowledges the discrepancy. Updated assessment confirms 8 fully completed sheds and 2 in final stages. Wastewater plant assessment is being arranged with an external engineering firm.",
        "response_date": date(2025, 12, 10),
        "supporting_evidence_url": None,
    },
    # Response for Gambella Irrigation
    {
        "id": VRES[2], "request_id": VREQ[5],
        "response_text": "Ministry of Agriculture confirms secondary channels are under construction. Revised coverage target is 6,500 hectares by end of 2026. Current functional irrigation covers 3,200 hectares.",
        "response_date": date(2025, 9, 15),
        "supporting_evidence_url": None,
    },
]

# ===========================================================================
# PUBLIC REPORTS
# ===========================================================================
PUBLIC_REPORTS = [
    {"id": PREP[1], "project_id": PROJ[1], "description": "The resurfaced road between Addis and Adama is excellent. Much safer driving conditions.", "photo_url": None, "location": "Addis\u2013Adama Expressway km 35", "report_date": date(2026, 4, 10), "status": "Acknowledged", "reporter_name": "Abebe T."},
    {"id": PREP[2], "project_id": PROJ[2], "description": "Observed unfinished factory buildings with exposed rebar. Workers not present on site during visit.", "photo_url": None, "location": "Hawassa Industrial Park", "report_date": date(2025, 10, 20), "status": "Incorporated", "reporter_name": "Hana M."},
    {"id": PREP[3], "project_id": PROJ[4], "description": "Construction on the light rail extension appears to have stalled near our neighborhood. No workers for weeks.", "photo_url": None, "location": "Ayat, Addis Ababa", "report_date": date(2025, 9, 5), "status": "Under Review", "reporter_name": "Dawit K."},
    {"id": PREP[4], "project_id": PROJ[8], "description": "The road to Wukro is still unpaved gravel. Buses frequently get stuck during rains.", "photo_url": None, "location": "Mekelle\u2013Wukro Road km 20", "report_date": date(2025, 7, 25), "status": "Incorporated", "reporter_name": "Gebremariam A."},
    {"id": PREP[5], "project_id": PROJ[9], "description": "The new riverside park near Kebena is beautiful. Great space for families.", "photo_url": None, "location": "Kebena Riverside, Addis Ababa", "report_date": date(2026, 1, 15), "status": "Acknowledged", "reporter_name": "Sara B."},
    {"id": PREP[6], "project_id": PROJ[11], "description": "Our farm has not received any irrigation water despite being within the project zone.", "photo_url": None, "location": "Gambella, Zone 2", "report_date": date(2025, 6, 20), "status": "Incorporated", "reporter_name": "Ojulu G."},
    {"id": PREP[7], "project_id": PROJ[7], "description": "The new hospital wing is operational and providing much-needed services to our community.", "photo_url": None, "location": "Jimma University Medical Center", "report_date": date(2026, 2, 28), "status": "Acknowledged", "reporter_name": "Fatuma A."},
    {"id": PREP[8], "project_id": PROJ[13], "description": "Wind turbines visible from the highway. Impressive to see renewable energy infrastructure.", "photo_url": None, "location": "Adama Wind Farm", "report_date": date(2025, 8, 10), "status": "Acknowledged", "reporter_name": "Yonas S."},
    {"id": PREP[9], "project_id": PROJ[14], "description": "Hospital building looks far from complete. Walls not plastered, no windows installed on upper floors.", "photo_url": None, "location": "Hawassa, Sidama", "report_date": date(2026, 1, 5), "status": "Under Review", "reporter_name": "Tigest W."},
    {"id": PREP[10], "project_id": PROJ[10], "description": "Enrolled for digital ID at Bole sub-city center. Process was smooth but took 3 hours waiting.", "photo_url": None, "location": "Bole Sub-City, Addis Ababa", "report_date": date(2025, 11, 20), "status": "Acknowledged", "reporter_name": "Kidist M."},
]


def seed_database(db_session):
    """Populate the database with mock data."""
    from app.models import (
        Institution, Project, Evidence, Discrepancy,
        VerificationRequest, VerificationResponse, PublicReport,
    )

    # Check if data already exists
    if db_session.query(Institution).first():
        return False  # Already seeded

    for data in INSTITUTIONS:
        db_session.add(Institution(**data))

    for data in PROJECTS:
        db_session.add(Project(**data))

    for data in EVIDENCE:
        db_session.add(Evidence(**data))

    for data in DISCREPANCIES:
        db_session.add(Discrepancy(**data))

    for data in VERIFICATION_REQUESTS:
        db_session.add(VerificationRequest(**data))

    for data in VERIFICATION_RESPONSES:
        db_session.add(VerificationResponse(**data))

    for data in PUBLIC_REPORTS:
        db_session.add(PublicReport(**data))

    db_session.commit()
    return True
