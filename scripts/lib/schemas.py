"""
Single source of truth for all data models.
Every engine imports from here. No schema duplication elsewhere.
"""

from __future__ import annotations
from enum import Enum
from typing import Literal
from pydantic import BaseModel


# ── LEAD PIPELINE ─────────────────────────────────────────────────────────────

class WebsiteSignals(BaseModel):
    quality_score: Literal["poor", "average", "good"] = "average"
    cms_detected: str | None = None
    has_booking_form: bool = False
    has_ssl: bool = True
    copyright_year: int | None = None
    fetch_status: Literal["success", "timeout", "error", "rate_limited"] = "success"


class SocialSignals(BaseModel):
    instagram_followers: int | None = None
    instagram_last_post_days: int | None = None
    instagram_post_frequency: Literal["daily", "weekly", "monthly", "dead"] | None = None
    facebook_last_post_days: int | None = None
    facebook_likes: int | None = None
    fetch_status: Literal["success", "not_found", "rate_limited"] = "success"


class RawProspect(BaseModel):
    place_id: str
    company_name: str
    owner_name: str | None = None
    phone: str
    website: str | None = None
    google_maps_url: str
    city: str
    state: str
    country: str = "US"
    address: str | None = None
    google_rating: float | None = None
    review_count: int | None = None
    last_google_review_date: str | None = None
    instagram_handle: str | None = None
    facebook_url: str | None = None
    scraped_at: str
    source_query: str
    niche: str


class EnrichedProspect(RawProspect):
    website_signals: WebsiteSignals | None = None
    social_signals: SocialSignals | None = None
    pain_signals: list[str] = []
    enriched_at: str


class ScoreDimension(BaseModel):
    name: str
    score: int
    weight: float
    evidence: str


class LeadScoreCard(BaseModel):
    company_name: str
    place_id: str
    scored_at: str
    dimensions: list[ScoreDimension]
    total_score: int
    tier: Literal["A", "B", "C", "D"]
    call_priority: int
    recommended_opener: str
    skip_reason: str | None = None


# ── CALL PIPELINE ─────────────────────────────────────────────────────────────

class CallOutcome(str, Enum):
    VOICEMAIL = "voicemail"
    HUNG_UP = "hung_up"
    GATEKEEPER_BLOCKED = "gatekeeper_blocked"
    INTERESTED = "interested"
    CALLBACK_SCHEDULED = "callback_scheduled"
    BOOKED = "booked"
    REJECTED = "rejected"
    DEAD = "dead"


class ObjectionInstance(BaseModel):
    exact_quote: str
    category: str
    caller_response: str
    response_quality: Literal["folded", "weak_pivot", "strong_pivot", "closed"]


class CoachingFlag(BaseModel):
    flag_type: str
    exact_quote: str
    severity: Literal["minor", "moderate", "critical"]
    coaching_note: str
    timestamp_hint: str | None = None


class CallAnalysis(BaseModel):
    transcript_file: str
    call_date: str | None = None
    prospect_name: str | None = None
    company_name: str | None = None
    phone: str | None = None
    outcome: CallOutcome
    outcome_confidence: float
    objections: list[ObjectionInstance] = []
    winning_phrases: list[str] = []
    rapport_moments: list[str] = []
    coaching_flags: list[CoachingFlag] = []
    filler_word_count: int | None = None
    close_attempted: bool = False
    close_type: Literal["specific_datetime", "vague", "no_attempt"] | None = None
    follow_up_date: str | None = None
    follow_up_action: str | None = None
    one_line_summary: str
    full_analysis: str


# ── COACHING ──────────────────────────────────────────────────────────────────

class PatternFinding(BaseModel):
    pattern: str
    frequency: int
    example_quotes: list[str]
    impact: Literal["helps", "hurts", "neutral"]
    fix: str


class CoachingReport(BaseModel):
    generated_at: str
    calls_analyzed: list[str]
    overall_grade: Literal["A", "B", "C", "D", "F"]
    confidence_score: int
    recurring_patterns: list[PatternFinding]
    top_3_wins: list[str]
    top_3_kills: list[str]
    drills: list[str]
    roast_text: str
    momentum_note: str
