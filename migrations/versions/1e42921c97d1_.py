"""empty message

Revision ID: 1e42921c97d1
Revises: b06eccb1084c
Create Date: 2023-03-27 07:59:23.360715

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e42921c97d1'
down_revision = 'b06eccb1084c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('character_has_episodes',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], ),
    sa.PrimaryKeyConstraint('character_id', 'episode_id')
    )
    op.create_table('character_has_locations',
    sa.Column('character_id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('character_id', 'location_id')
    )
    op.create_table('episode_has_locations',
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episodes.id'], ),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('episode_id', 'location_id')
    )
    op.drop_table('episodes_locations')
    op.drop_table('characters_episodes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters_episodes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_character', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_episode', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_character'], ['characters.id'], name='characters_episodes_id_character_fkey'),
    sa.ForeignKeyConstraint(['id_episode'], ['episodes.id'], name='characters_episodes_id_episode_fkey'),
    sa.PrimaryKeyConstraint('id', name='characters_episodes_pkey')
    )
    op.create_table('episodes_locations',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id_episode', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id_location', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['id_episode'], ['episodes.id'], name='episodes_locations_id_episode_fkey'),
    sa.ForeignKeyConstraint(['id_location'], ['locations.id'], name='episodes_locations_id_location_fkey'),
    sa.PrimaryKeyConstraint('id', name='episodes_locations_pkey')
    )
    op.drop_table('episode_has_locations')
    op.drop_table('character_has_locations')
    op.drop_table('character_has_episodes')
    # ### end Alembic commands ###
