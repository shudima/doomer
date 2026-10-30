"""Private progress, finished topics and reactions."""
from alembic import op
import sqlalchemy as sa

revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    schema = 'doomer' if op.get_bind().dialect.name == 'postgresql' else None
    op.create_table('topic_state',
        sa.Column('user_id', sa.String(128), primary_key=True),
        sa.Column('topic_id', sa.String(250), primary_key=True),
        sa.Column('doom_id', sa.String(300), nullable=False),
        sa.Column('version', sa.Integer(), nullable=False),
        sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()), schema=schema)
    op.create_table('reaction',
        sa.Column('user_id', sa.String(128), primary_key=True),
        sa.Column('doom_id', sa.String(300), primary_key=True),
        sa.Column('value', sa.String(7), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
        sa.CheckConstraint("value IN ('like', 'dislike')", name='valid_reaction'), schema=schema)

def downgrade():
    schema = 'doomer' if op.get_bind().dialect.name == 'postgresql' else None
    op.drop_table('reaction', schema=schema)
    op.drop_table('topic_state', schema=schema)
